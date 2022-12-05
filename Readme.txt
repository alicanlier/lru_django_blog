#Album 만들기에 필요한 과정

### Pillow library를 활용 하여...

1. Album table
2. 사진을 사이트에 등록하는 업로드 기능
3. 썸네일 사진을 생성하는 기능

국체적 작업순서
<1>. photo app을 만든다.
<2>. photo app을 등록한다.
<3>. Admin site에 보이도록 모델을 등록
<5>. fields.py에 ThumbnalImageField custom field를 정의 해줌
<6>. make migrations 수행 ~ 모델을 데이타베이스에 반영
<7>. migrate
<8>. url에 정의 - URLconf 코딩
<9>. 뷰코딩 - views.py - 뷰로직작성
<10> templates 디렉토리 templates file 작성

##############################################
3 10장 - 인증 기능
# Login username, password + login한 사용자에게 권한 부여
# 장고엔진 - web요청에 따른 사용자 식별, 사용자별 세션할당, 관리기능
# 1. Login, logout
# 2. 회원가입
# 3. 비밀번호 변경
# 4. 11장, 12장 ~ Login시 부여되는 기본 권한에 따라 기존 콘텐츠의 생성 및 수정기능
###############################################
# 구체적 작업 ~
# 1. django.contrib.auth 인증기능 담당 앱, 이 앱의 기능을 정확하게 이해/사용
# 2. django가 기본으로 제공하는 user table ==> 확장/변경
# 3. url설계 변경
# 4. widget_tweaks 앱 등록 ==> settings.py
# 5. HomeView 작성 ==> migrate
# 6. Home.html 작성, 상속기능 적용 (base.html)
# 7. LOGIN_REDIRECT_URL 상수를 settings.py에 지정 (LOGIN_URL, LOGOUT_REDIRECT_URL)
# 8. url.py ==> URL 정의
# 9. View logic작성 ==> views.py (mvc pattern's control에 해당함)
# 10. template 작성 ==> *.html작성(mvc pattern's view에 해당함)
###############################################
# 11. 콘텐츠 편집 기능(Bookmark, Blog)
# 기본적으로 관리자는 수정, 삭제 등이 모두 가능하지만 모든 사용자에게 이러한 권한을 모두 부여할 수 없다.
# 일반사용자도 저절한 수준의 콘텐츠 생성 및 변경 권한이 있어야한다.
# <1> Contents에 대한 열람은 모든 사용자가 가능하게
# <2> Contents를 새로이 생성하는 것은 로그인한 사용자만 가능하도록
# <3> Contents를 수정 또는 삭제하는 작업은 그 Contents를 생성한 사용자만 가능하게 
# base.html에 menu 를 추가 ==> [Add]~추가, [Change]~수정, 삭제
###############################################
# 구체적 작업 사항
# Bookmark model을 변경 ~ owner필드를 추가 ~ 포린키로 생성(1측table User)
# Post model 변경 ~ owner field를 추가 ~ foreign key로 생성 ( " )
# 추가한 메뉴에 관련된 url 추가 (Bookmark앱의 urls.py, blog앱의 urls.py)
# migrations
# migrate
# view coding ~ views.py
# templates directory ==> templates file과 403.html
################################################
# 126장 콘텐츠 편집 기능(Photo앱) - Java's CRUD
# Photo App은 2개의 table 있어 각각의 편집 기능이 필요
# Album과 Photo table은 1:다 관계로 연결되어 있어, 생성이나 수정 폼 
# 화면에서 이런 관계가 어떻게 구현 되는지 이해하는 것이 중요
# 11장에 적용한 권한 요구 사항이 이번 장에도 그대로 적용
# 즉, 1. Contents에 대한 열람은 모든 사용자가 사용 가능
# 2. Contents를 새로 생성하는 것은, login한 사람 마ㅜ
# 3. Contents를 수정 또는 삭제하는 작업은 그 contents를 생성한 사용자만 가능
# 1:다 관계를 지원하는 폰셑을 사용 ~ PhotoInlineFormSet
################################################
# 구체적 작업
# 1. Album table에 owner field추가 (부수적 작업: migrations==>migrate)
# 2. URLConf 코딩 작업
# 3. 콘트롤러 - 뷰코딩(forms.py, views.py)
# 4. templates directory 템플릿파일 작성하고(below), home.html수정
# photo_form.html, photo_change_list.html, photo_confirm_delete.html, 
# album_form.html, album_change_list.html, album_confirm_delete.html
################################################


