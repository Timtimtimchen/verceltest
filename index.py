from flask import Flask,render_template,send_file

app = Flask(__name__,static_url_path="/resume")

@app.route("/")
def index():
    # 请替换 '你的PDF文件.pdf' 为你要显示的实际PDF文件的路径和文件名
    pdf_path = 'static\\履歷.pdf'
    # 使用send_file函数发送PDF文件
    return send_file(pdf_path, as_attachment=False)

app.run(debug = True)

