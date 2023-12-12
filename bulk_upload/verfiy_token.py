def verify_token(request):
    token = request.headers.get('AUTHORIZATION', '')[7:]
    if not token:
        return False, "Token Not verified"
    return True, "Token Verified"
