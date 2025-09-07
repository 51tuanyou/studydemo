from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chat.graph.quote_graph import quote_graph
from chat.serializers import QuoteRequestSerializer


class QuoteAPIView(APIView):
    """
    POST 请求：
    {
        "email_text": "...",
        "user_type": "default"
    }
    返回：
    {
        "iPhone 15": {"price": 523, "source": "internal"},
        "Galaxy S23": {"price": 1200, "source": "web"}
    }
    """

    def post(self, request):
        serializer = QuoteRequestSerializer(data=request.data)
        if serializer.is_valid():
            email_text = serializer.validated_data['email_text']
            user_type = serializer.validated_data['user_type']

            # 调用 LangGraph 图谱
            outputs = quote_graph.run(input={
                "input_text": email_text,
                "user_type": user_type
            })

            final_result = outputs.get("final_result", {})
            return Response(final_result)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
