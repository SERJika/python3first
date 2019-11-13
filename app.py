from flask import Flask, request, render_template # render_template, который включает функции для Jinja
import datetime

app = Flask(__name__)  # объявим экземпляр фласка

now = datetime.datetime.now()

videos = [
    {
        "id":"0",
        "title":"Продажа квартиры, купленной с использованием материнского капитала",
        "url":"XOxGQRNY0qY"
    },
    {
        "id":"1",
        "title":"Продажа ипотечной квартиры с материнским капиталом",
        "url":"aO7QpKgtpJA"
    },
    {
        "id":"2",
        "title":"Как рассчитывать доли детей в квартире, приобретенной с материнским капиталом",
        "url":"17B8VoP6koc"
    },
    {
        "id":"3",
        "title":"Занижение стоимости квартиры в договоре купли-продажи квартиры",
        "url":"zvPtYIV4dEQ"
    },
    {
        "id":"4",
        "title":"Как не лишиться квартиры при признании продавца банкротом",
        "url":"Rd3Si_JM2Dc"
    },
    {
        "id":"5",
        "title":"Совместная собственность. Брачный договор",
        "url":"v6_RAxRbydw"
    },
    {
        "id":"6",
        "title":"Покупка квартиры",
        "url":"G9CH-6tDJKA"
    },
    {
        "id":"7",
        "title":"Порядок оформления недвижимости в собственность по наследству",
        "url":"sVT-1HzQXn0"
    },
    {
        "id":"8",
        "title":"Кабальная сделка. Что это такое и как ее оспорить в суде",
        "url":"AHCfQ-2L-F4"
    },
    {
        "id":"9",
        "title":"Как расторгнуть договор купли-продажи квартиры",
        "url":"lpm5fguzoz4"
    },
    {
        "id":"10",
        "title":"Особенности сделок с недвижимостью с участием несовершеннолетних и недееспособных",
        "url":"GGnSP0Gg_-w"
    },
    {
        "id":"11",
        "title":"Как признать наследника недостойным",
        "url":"9Fhx7bXppMA"
    },
    {
        "id":"12",
        "title":"По каким долгам не отвечают наследники",
        "url":"h_HLjJ47pJA"
    },
]

tags = {
    "kidsmoney": {
        "title": "материнскийкапитал",
        "videos" : [0,1,2]
    },
    "bankmoney": {
        "title": "ипотека",
        "videos" : [1]
    },
    "deals": {
        "title": "проведениесделки",
        "videos": [6, 8, 9, 10]
    },
    "inheritance": {
        "title": "наследство",
        "videos": [7, 11, 12]
    },
    "other": {
        "title": "разное",
        "videos": [3, 4, 5]
    },
}

video_tags = {}
for i in range(len(videos)):
    video_tags[i] = {}
    for key, val in tags.items():
        if i in val['videos'] and val['title'] not in video_tags:
            video_tags[i].update({key:val['title']})

playlists = {
    "estate_sale": {
        "title"  : "О продаже недвижимости",
        "videos" : [0,1,3,4,6]
    },
    "property_registration": {
        "title"  : "Оформление собственности",
        "videos" : [2,5,7]
    },
    "apartments_purchase": {
        "title" : "Покупка квартиры",
        "videos": [6]
    },
    "estate_miscellaneous": {
        "title" : "Разное о недвижимости",
        "videos": [8, 9, 10, 11, 12]
    },
}

playlists_first_els = {}
plist_counter = 0
for key in playlists.keys():
    plist = playlists[key]
    if plist_counter < 3:
        playlists_first_els[key] = plist['title']
        plist_counter += 1

@app.route('/')
def main():
    return page_index = render_template("main.html",
        menu=['active','','',''],
        favicon="static/img/favicon.ico",
        logo_url="static/img/logo.png",
        tags=tags,
        playlists=playlists_first_els,
        intro_img_url="static/img/house-care.jpg",
        now_year=now.year,
        dev_name='serjica')

@app.route('/about/')
def about():
    return page_about = render_template("about.html",
        menu=['','active','',''],
        favicon="static/img/favicon.ico",
        logo_url="static/img/logo.png",
        tags=tags,
        playlists=playlists,
        intro_img_url="static/img/house-care.jpg",
        now_year=now.year,
        dev_name='serjica')

@app.route('/contacts/')
def contacts():
    return page_contacts = render_template("contacts.html",
        menu=['','','','active'],
        favicon="static/img/favicon.ico",
        logo_url="static/img/logo.png",
        tags=tags,
        playlists=playlists,
        now_year=now.year,
        dev_name='serjica')

@app.route('/videos/<id>')
def videos_page(id):
    return page_video = render_template("video.html",
        menu=['', '', '', ''],
        favicon="static/img/favicon.ico",
        logo_url="static/img/logo.png",
        tags=video_tags[int(id)],
        videos=videos,
        id=int(id),
        now_year=now.year,
        dev_name='serjica')

@app.route('/tags/<tag>')
def thetag(tag):
    return page_tag = render_template("tag.html",
        menu=['', '', 'active', ''],
        favicon="static/img/favicon.ico",
        logo_url="static/img/logo.png",
        tags=tags[tag],
        videos=videos,
        now_year=now.year,
        dev_name='serjica')

@app.route('/playlists/')
def playlist():
    return page_playlists = render_template("playlists.html",
        menu=['', '', 'active', ''],
        favicon="static/img/favicon.ico",
        logo_url="static/img/logo.png",
        tags=tags,
        playlists=playlists,
        now_year=now.year,
        dev_name='serjica')

@app.route('/playlists/<list>')
def theplaylist(list):
    return page_playlist = render_template("playlist.html",
        menu=['', '', 'active', ''],
        favicon="static/img/favicon.ico",
        logo_url="static/img/logo.png",
        tags=tags,
        playlists=playlists[list],
        videos=videos,
        now_year=now.year,
        dev_name='serjica')

@app.errorhandler(404)
def page_not_found(error):
    return page_404 = render_template("404.html",
        menu=['','','',''],
        favicon="static/img/favicon.ico",
        logo_url="static/img/logo.png",
        tags=tags,
        playlists=playlists,
        now_year=now.year,
        dev_name='serjica')

if __name__ == '__main__':
    app.run()
