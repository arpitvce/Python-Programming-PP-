from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi import Form
from fastapi import FastAPI

app=FastAPI()


@app.get('/',response_class=HTMLResponse)
def form():
    return """

    <html>
        <body>
        <h2>Add Two Numbers</h2>
        <form action="/add" method="POST">
            <input type="number" name="a" placeholder="Enter A:" requrired>
            <input type="number" name="b" placeholder="Enter B:" required>
            <button type="submit"> ADD</button>
            <button type="submit"> Multiply </button>
            </form>
        </body>
    </html>
    """

@app.post('/add')
def form(a:int=Form(...),b:int=Form(...)):
    return {"sum":a+b}


