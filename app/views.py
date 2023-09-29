# from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .actions import get_gpt3_response
import json
from app.gspread import update_sheet

# Key = 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

# Create your views here.
class mcqView(APIView):
    def post(self,request):
        data = request.data
        prompt = f"create {data['questions']} questions on {data['topic']} having all the questions\
              covered on {data['subtopic']} with {data['level']} difficulty having {data['type']} type in mcq pattern and also\
                  provide the answers for the same. The questioons shoulld not be repeated in any way. There should be\
                      no grammatical mistakes in the questions. there should be accurate answers for the questions no two options\
                          should be same. The output should be in json format. The format of the json should be as follows:\
                            for conceptual questions:\
                                question,options(array),answer\
                                    for guessing questions:\
                                        question,code,options(array),answer\
                                            and the key should be questions only and the question \
                                    should not contain the code the code should be only in the code \
                                        field. There should be exactly 4 options for each question."
        res = get_gpt3_response(prompt)
        content = res.choices[0].message.content
        content = content.replace('\n','')
        content = content.replace('\\n','')
        content = content.replace('\\','')
        json_data = json.loads(content)
        update_sheet(json_data,"Questions",data['topic'],data['subtopic'])
        return Response(json_data)


class createBlogView(APIView):
    def post(self,request):
        data = request.data
        # prompt = f"create a blog on {data['topic']} which has more accuracy and have all the aspects covered which are important."
        prompt = f"Write your blog content here on {data['topic']}. You can include important information, facts, and details about the topic you want to cover. Ensure that the content is well-structured and ready to be converted into an HTML and CSS-based blog post."
        res = get_gpt3_response(prompt)
        return Response(res.choices[0].message.content)
    
class convertContentToBlogPage(APIView):
    def post(self,request):
        data = request.data
        # prompt = f"create a blog page using HTML and CSS on {data['content']} which is in {data['theme']} theme. \
        #     The styling should be there in the head tag iteself.\
        #     Ignore the backslash n and backslash from the content.\
        #     The blog page should be styled in a proper blog page format and should be responsive."

        prompt = f"{data['content']}. convert this to a blog in {data['theme']} theme using html and css only include the body and style tag.All the escape characters should be removed.\
            the sections should be properly aligned.\
                The blog page should be styled in a proper blog page format and should be responsive."
        res = get_gpt3_response(prompt)
        temp = res.choices[0].message.content
        temp = temp.replace('\n','')
        temp = temp.replace('\\','')
        return Response(temp)