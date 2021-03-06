CAFESCAN - 자리창출넘버원
=============

1.ppt 발표자료
-------------
>http://bitly.kr/3Mj70

2.무엇을 만드는가?
-------------
>주변 카페의 좌석 현황, 혼잡도 정보를 제공하는 앱

3.시스템 구성도
-------------
>![system](https://user-images.githubusercontent.com/48238562/56094223-d63bcb80-5f0c-11e9-9cd3-92a7245f1d84.png)

4.데이터 흐름도
-------------
1. 회로 연결
    - NodeMCU는 Arduino를 이용하여 소스코드를 업로드한다. 이 소스코드는 HC_SR04(초음파 거리 센서)를 이용하여 30초 마다 100번의 거리를 측정하여 이를 서버로 전송한다.
2. 데이터 전송
    - Node MCU
        + 측정용 NodeMCU는 HC_SR04 모듈로 측정한 100개의 거리 데이터를 30초마다 WiFi를 이용하여 AMAZON Web Service에서 제공하는 EC2 서버에 실시간으로 전달한다.
        + 머신러닝용 NodeMCU는 HC_SR04 모듈로 30초 동안 측정된 100개의 거리 데이터는 하나의 유닛으로 하여 100번째 측정 후 장애물 감지 센서를 이용해 좌석의 유무를 라벨링하여 서버 전송한다.이렇게 만들어진 Labels of training set은 머신러닝에 사용된다. 
    - AMAZON EC2
        + AMAZON EC2는 클라우드 형태로 제공되며 UBUNTU LINUX 기반의 서버로 운영된다.
3. 데이터 가공
    - AMAZON EC2
        + AWS EC2 서버는 지속적으로 운영되며 NodeMCU에서 데이터를 받고 분류 및 데이터베이스 위한 프로그램을 유지시킨다.
    - Node. js
        + AWS EC2 서버에서 받은 데이터는 node.js로 작성된 코드에 따라 DB에 저장된다.
    - MySQL
        + MySQL은 분류된 값과 등록된 시간 값을 같이 데이터베이스로 저장하며 데이터는 계속 누적된다.
    - Machine Learning
        + Python의 keras를 이용해 Labels of training set을 바탕으로 supervised learning을 해서 머신러닝 모델을 만든다.
    - HTML
        + 저장된 데이터들을 이용해서 시간, 요일별 통계치를 얻어 웹 페이지에 표현한다.
4. 데이터 사용
    - 좌석의 현황
        + 측정용 NodeMCU에서 30초간 측정된 100개의 거리 data 유닛이 들어오면 머신러닝 모델이 좌석이 있으면 1, 없으면 0을 DB로 출력한다
    - 카페 혼잡도
        + 한 카페의 전체 좌석과 이용 중인 좌석을 가지고 혼잡도를 계산할 수 있다.
       
(기술개발 과정)
추가
