from app import app



from flask_wtf.csrf import generate_csrf
# 调用函数生成 csrf_token
@app.after_request
def after_request(response):
    # 调用函数生成 csrf_token
    csrf_token = generate_csrf()
    # 通过 cookie 将值传给前端
    response.set_cookie("csrf_token", csrf_token)
    return response






