import functions_framework

@functions_framework.http
def helloworld(request: dict):

  return {
    "message": "hello world v2.0",
  }, 202