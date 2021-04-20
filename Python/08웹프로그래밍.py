{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Django\n",
    "\n",
    "# 환경변수 -> path 확인 -> C:\\Anaconda3     C:\\Anaconda3\\Scripts      \n",
    "\n",
    "# cmd -> pip install Django\n",
    "\n",
    "# 작업 폴더로 이동 -> django-admin startproject mysite      프로젝트 생성\n",
    "\n",
    "# cd mysite 이동 -> python manage.py runserver              웹서버 실행. 서버는 종료하면 안된다.\n",
    "\n",
    "# 웹브라우저 -> http://localhost:8000                       Django 시작페이지 요청\n",
    "\n",
    "# 새로 cmd -> mysite 폴더 이동 > python manage.py startapp bookmark        bookmark 웹어플리케이션 생성\n",
    "\n",
    "# mysite\\mysite\\settings.py 열어서 편집\n",
    "#      33 INSTALLED_APPS = [..., 'bookmark',]              어플리케이션 등록\n",
    "#      107 LANGUAGE_CODE='ko-kr'                           한글 설정으로 변경\n",
    "#      109 TIME_ZONE='Asia/Seoul'                          변경. 대소문자 주의\n",
    "\n",
    "# CTRL + BREAK                                             서버 종료\n",
    "#       mysite\\settings.py changed, reloading. 메시지 확인\n",
    "# mysite> python manage.py runserver                       서버 다시 시작\n",
    "\n",
    "# 웹브라우저 -> http://localhost:8000                       영어페이지가 한글로 변경\n",
    "\n",
    "\n",
    "# mysite> python manage.py migrate                          SQLite 파일을 데이터베이스 형식으로 변경\n",
    "# mysite> python manage.py createsuperuser                  관리자 계정 생성\n",
    "#         아이디 : admin\n",
    "#         이메일 : 엔터\n",
    "#         password : 1234     경고는 무시하고 y 누른 후 엔터\n",
    "# mysite> python manage.py migrate\n",
    "\n",
    "# 웹브라우저 -> http://localhost:8000/admin/                 SQLite 관리자계정 로그인\n",
    "#         아이디 : admin\n",
    "#         암호 : 1234"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## bookmark 어플리케이션 ##\n",
    "\n",
    "# Model #\n",
    "# 테이블 생성\n",
    "\n",
    "\n",
    "\n",
    "# 테이블을 Admin 페이지에 등록\n",
    "\n",
    "\n",
    "# Admin 계정에서 데이터를 insert\n",
    "\n",
    "\n",
    "\n",
    "# Template #\n",
    "# 사용자 페이지를 생성\n",
    "\n",
    "\n",
    "\n",
    "# View #\n",
    "# views 처리와 출력 설정을 등록\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
