# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов


from flask import Flask

app = Flask(__name__)


@app.route("/about")
def about_company():
    return "<p><b>Some information about company</b></p>"


@app.route("/contacts")
def contacts_information():
    return """
            <html>
                <h1>Our Contacts</h1>
                <ol>
                    <li>- Phone Number: +7***</li>
                    <li>- TG Account: @****</li>
                    <li>- Adress: Не скажу</li>
                </ol>
            </html>"""


@app.route("/posts")
def posts_list():
    return """
            <html>
                <h1>All Posts</h1>
                <table>
                    <tr>
                        <th>Number</th>
                        <th>Post name</th>
                        <th>Date</th>
                    </tr>
                    <tr>
                        <th>1</th>
                        <th>Dogs</th>
                        <th>18.06.2024</th>
                    </tr>
                    <tr>
                        <th>2</th>
                        <th>Cats</th>
                        <th>17.02.2025</th>
                    </tr>
                </table>
            </html>"""
