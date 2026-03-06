from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# ఇక్కడ చూడు, GET తో పాటు POST కూడా యాడ్ చేశాం!
@api_view(['GET', 'POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
def get_students(request):
    
    # 1. ఒకవేళ ఎవరైనా డేటా అడిగితే (GET)
    if request.method == 'GET':
        # 1. --- Search Logic (వెతకడం) ---
        search_query = request.GET.get('search', '') # ఎవరైనా ?search= అని అడిగితే...
        if search_query:
            # పేరులో ఆ అక్షరాలు ఉన్న వాళ్ళని ఫిల్టర్ చేస్తాం (icontains అంటే Case Insensitive)
            students = Student.objects.filter(name__icontains=search_query)
        else:
            students = Student.objects.all()
        # 2. --- Pagination Logic (పేజీలుగా విడగొట్టడం) ---
        paginator = PageNumberPagination()
        paginator.page_size = 2 # టెస్టింగ్ కోసం ఒక పేజీకి కేవలం 2 రికార్డ్స్ మాత్రమే పంపుతున్నాం
        result_page = paginator.paginate_queryset(students, request)

        # 3. డేటాని పంపించడం
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    # 2. ఒకవేళ ఎవరైనా కొత్త డేటా పంపిస్తే (POST)
    elif request.method == 'POST':
        # వాళ్ళు పంపిన డేటాని (request.data) సీరియలైజర్ కి ఇస్తున్నాం
        serializer = StudentSerializer(data=request.data) 
        
        # డేటా కరెక్ట్ గా ఉందో లేదో చెక్ చేస్తున్నాం
        if serializer.is_valid():
            serializer.save() # డేటాబేస్ లోకి సేవ్ చేస్తున్నాం!
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # డేటా తప్పుగా ఉంటే ఎర్రర్ చూపిస్తాం
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ఇందాక రాసిన get_students ఫంక్షన్ పైన ఉంటుంది, దాన్ని అలాగే వదిలేయ్.
# దాని కింద ఈ కొత్త ఫంక్షన్ యాడ్ చెయ్:

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk): # pk అంటే Primary Key (లేదా ID)
    
    # ముందుగా ఆ ID తో స్టూడెంట్ ఉన్నాడో లేదో వెతుకుతాం
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    # 1. GET: ఆ ఒక్క స్టూడెంట్ డేటా మాత్రమే చూడటానికి
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # 2. PUT: ఉన్న డేటాని అప్‌డేట్ (Edit) చేయడానికి
    elif request.method == 'PUT':
        # పాత స్టూడెంట్ డేటాని, కొత్తగా వచ్చిన డేటాతో (request.data) రీప్లేస్ చేస్తున్నాం
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save() # అప్‌డేట్ అయిన డేటా సేవ్ అవుతుంది
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. DELETE: ఆ స్టూడెంట్ ని డేటాబేస్ నుంచి తీసేయడానికి
    elif request.method == 'DELETE':
        student.delete()
        return Response({'message': 'Student deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)