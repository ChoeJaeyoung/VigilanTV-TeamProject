<%@page import="java.util.Date"%>
<%@page import="java.text.SimpleDateFormat"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE HTML>
<!--
   Twenty by HTML5 UP
   html5up.net | @ajlkn
   Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
<% 
String jsonPlate = (String)request.getAttribute("carNumber");
String path = (String)request.getAttribute("path");
String saveFileName = (String)request.getAttribute("saveFileName");

SimpleDateFormat format1 = new SimpleDateFormat ( "yyyyMMddHHmmss");
Date time = new Date();
String connectionTime = format1.format(time);
//String connectionTime2 = "20190219181124";
System.out.println("CONNECTION TIME : "+connectionTime);
%>

<%
if(path!=null && saveFileName!=null){
%>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script type="text/javascript">
setInterval(function () {
    $.ajax({
        url: 'testajax',
        type: 'GET',
        data: { connectionTime: "<%=connectionTime%>"} ,
        dataType: 'json',
        error : function(){
        	$( "#result" ).append( "" );
        },
        success: function(args) {
        	console.log('success');
	        /*$.each(args, function(index, value) {
	        console.log(index + " : " + args[index]);
	        });   */
	        $("#result").empty();
	        for(var i =0; i<7; i++){
	        	var value = args[i]
	        	var json = JSON.parse(value)
	        	var date = json.date_detect
	        	var year = date.substring(0,4)
	        	var month = date.substring(4,6)
	        	var day = date.substring(6,8)
	        	var time = json.time_detect
	        	var hour = time.substring(0,2)
	        	var min = time.substring(2,4)
	        	var sec = time.substring(4,6)
		        $("#result").append("<tr text-align='center' scope='rows' bgcolor='white'><td text-align='center'>"+json.plate_num+"</td><td text-align='center'>"+ year + "년 " + month + "월 " + day + "일  (" + hour + "시 " + min + "분 " + sec + "초" + ")</td></tr>");
	        	
	        }
	        
        }
    });
}, 5000);
</script>
<%
}
%>
   <head>
      <title>VIGILANTV</title>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
      <link rel="stylesheet" href="resources/assets/css/main.css" />
      <noscript><link rel="stylesheet" href="resources/assets/css/noscript.css" /></noscript>
      <style>
      #file { width:0; height:0; }
      #center {width: 100px height:100px}
      .text {
		  width: 100%;
		  box-sizing: border-box;
		  border: 2px solid #ccc;
		  border-radius: 4px;
		  font-size: 16px;
		  background-color: white;
		  background-image: url('searchicon.png');
		  background-position: 10px 10px;
		  background-repeat: no-repeat;
		  padding: 12px 20px 12px 40px;
		  -webkit-transition: width 0.4s ease-in-out;
		  transition: width 0.4s ease-in-out;
		}
		
		table.type09 {
			border-collapse: collapse;
			text-align: left;
			line-height: 1.5;

		}

		table.type09 thead th {
			padding: 10px;
			font-weight: bold;
			vertical-align: top;
			color: #369;
			border-bottom: 3px solid #036;
		}

		table.type09 tbody th {
			width: 150px;
			padding: 10px;
			font-weight: bold;
			vertical-align: top;
			border-bottom: 1px solid #ccc;
			background: #f3f6f7;
		}

		table.type09 td {
			width: 350px;
			padding: 10px;
			vertical-align: top;
			border-bottom: 1px solid #ccc;
			align: center;
		}
		.carnum {color:#5D5D5D;}
		.button{width:50px;}
		@font-face {
	        font-family: webisfree;
	        src: url('resources/output/KakaoRegular.ttf');
	    }
	      
	    body {
	        font-family: webisfree;
	    }
      </style>
   </head>
   <body class="index is-preload">
      <div id="page-wrapper">

         <!-- Header -->
            <header id="header" class="alt">
               <h1 id="logo"><a href="">VIGILANTV <span>by 2조</span></a></h1>
               <nav id="nav">
                  <ul>
                     <li class="current">Welcome</li>
                     <li><a href="carcheck" class="button primary">조회하기</a></li>
                  </ul>
               </nav>
            </header>

         <!-- Banner -->
            <section id="banner">

               <!--
                  ".inner" is set up as an inline-block so it automatically expands
                  in both directions to fit whatever's inside it. This means it won't
                  automatically wrap lines, so be sure to use line breaks where
                  appropriate (<br />).
               -->
               <div class="inner">

                  <header>
                     <h2>VIGILANTV</h2>
                  </header>
                  <p>딥러닝 기반
                  <br />
                  <strong>불법 주·정차 자동 탐지 시스템<strong/>
                  <br />
                  </p>
                  <footer>
                     <ul class="buttons stacked">
                        <li><a href="#main" class="button fit scrolly">START</a></li>
                     </ul>
                  </footer>

               </div>

            </section>

         <!-- Main -->
            <article id="main">

               <header class="special container">
                  <span class="icon fa-bar-chart-o"></span>
                  <h2><strong>CCTV 영상 분석하기</strong>
                  </h2>
                  <p>분석 결과로 어린이 보호구역 CCTV 영상 속 불법 주·정차 차량의 <strong>차량 번호, 과금 정보, 증거 사진</strong>을 확인 할 수 있습니다.
                  <br />
               </header>

               <!-- One -->
                  <section class="wrapper style2 container special-alt">
                     <div class="row gtr-50">
                        <div class="col-8 col-12-narrower">

                           <header>
                              <h2>분석할 영상 선택</h2>

                           </header>
                           <br/>
                           <p>분석하고자하는 어린이 보호구역 CCTV 영상을 업로드하면 됩니다.
                           <footer>
                              <form action="fileUpload" method="post" enctype="multipart/form-data">
                                 <input type="file" value="파일 업로드" name="file" class="upload"></br></br>
                                 <input type="submit">
                              </form>
                            
                           </footer>
                        </div>
                       
                     </div>
                     <div class="video-streaming">
                        <br><br>
                        <table style="margin-left: auto; margin-right: auto; text-align: center;" >
                           <tr>
                              <td>
                              <%
                              if(path!=null && saveFileName!=null){
                                 %>
                                 <iframe src="http://192.168.1.51:5000/streaming/<%=saveFileName%>?path='<%=path%>'"  frameborder="0" width="960" height="540" scrolling="no"></iframe>
                                 <%
                              }
                              %>
                              </td>
                           </tr>
                        </table>
                     </div>
                     
	                 <span style="font-size:20pt; color:black">
	                        <%
                              if(path!=null && saveFileName!=null){
                                 %>
                                 <table id='type09'>
			                        <thead>
			                        <tr text-align='center' scope='rows' bgcolor='#F6F6F6'>
				                        <td>차량번호</td>
				                        <td>시작시각</td>
			                        </tr>
			                        </thead>
			                        <tbody id='result'>
			                        </tbody>
			                        
		                        </table>
		                        <%
                              }
                              %>

                    </span>
                    </div>
                     
                  </section>

               <!-- Two -->
                  <section class="wrapper style1 container special">
                     <div class="row">
                        <div class="col-4 col-12-narrower">

                           <section>
                              <span class="icon featured fa-check"></span>
                              <header>
                                 <h3>DETECTION</h3>
                              </header>
                              <p>YOLO 모델을 활용하여 영상 속 자동차만을 자동적으로 검출한다. 또한, 직접 자동차 번호판 객체를 학습시켜 자동차만을 검출한 프레임에서 번호판을 검출한다.</p>
                           </section>

                        </div>
                        <div class="col-4 col-12-narrower">

                           <section>
                              <span class="icon featured fa-check"></span>
                              <header>
                                 <h3>TRACKING</h3>
                              </header>
                              <p>SORT 트래킹 기술을 사용하여 자동차를 추적한다. 자동차마다 고유 아이디를 부여하여 측정한 시간을 기준으로 불법 주·정차 차량을 판단한다.</p>
                           </section>

                        </div>
                        <div class="col-4 col-12-narrower">

                           <section>
                              <span class="icon featured fa-check"></span>
                              <header>
                                 <h3>OCR</h3>
                              </header>
                              <p>Tesseract OCR을 활용하여 현재 자동차 번호판에 사용되는 한글 글자와 숫자들을 폰트로 학습시켜 모델을 재생성하였다. 재생성한 모델을 기존의 모델과 결합하여 보다 정확한 차량 번호 인식이 가능하다. </p>
                           </section>

                        </div>
                     </div>
                  </section>

               <!-- Three -->
                  <section class="wrapper style3 container special">

                     <header class="major">
                        <h2><strong>영상 분석 과정</strong></h2>
                     </header>

                     <h3>[ 차량 인식 및 추적 ]</h3>
                     <p>어린이 보호구역 CCTV 영상에 등장하는 모든 자동차들을 </br>
                        자동으로 인식해 고유 ID를 부여하고, 이를 추적하여 ID 별 시간을 측정한다.
                     </p>
                     <div class="row">
                        <div class="col-6 col-12-narrower">

                           <section>
                              <a href="#" class="image featured"><img src="resources/output/img_id1.0_f10.jpg" alt="" /></a>
                           </section>

                        </div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <a href="#" class="image featured"><img src="resources/output/img_id4.0_f10.jpg" alt="" /></a>
                           </section>

                        </div>
                     </div>
                     <br/>
                     <div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <img src="resources/output/arrow.png" alt="" class = "center" /></br>
                              <img src="resources/output/tab.JPG" alt="" class = "center"/>
                           </section>
                        </div>

                     </div>


                     <h3>[ 불법 주·정차 차량 탐지 ]</h3>
                     <p>어린이 보호구역 불법 주·정차 차량으로 판단되는 차량의 증거 사진을 수집한다.
                        <br/>
                        동일한 차량이 1분이상 등장하는 순간 첫 사진을 수집하고, 해당 차량이 지속적으로 등장할 시
                        <br/>
                        매 시간 별 증거 사진을 수집하여 보관한다.
                     </p>
                     <div class="row">
                        <div class="col-6 col-12-narrower">

                           <section>
                              <a href="#" class="image featured"><img src="resources/output/box_id1.0_f10.jpg" alt="" /></a>
                           </section>

                        </div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <a href="#" class="image featured"><img src="resources/output/box_id4.0_f10.jpg" alt="" /></a>
                           </section>

                        </div>
                     </div>
                     </br>
                     <div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <img src="resources/output/arrow.png" alt="" /></br>
                              <img src="resources/output/tab.JPG" alt="" />
                           </section>
                        </div>

                     </div>


                     <h3>[ 차량 번호판 인식 및 이미지 전처리 ]</h3>
                     <p>차량 번호판을 인식하여 OCR에 가장 적합한 이미지로 전처리 작업을 거친다.<br/>
                        : 왜곡보정, Grayscale, Blur처리, 이진화, 노이즈 제거 과정
                     </p>
                     <br/>
                     <div class="row">
                        <div class="col-6 col-12-narrower">

                           <section>
                              <a href="#" class="image featured"><img src="resources/output/num01.png" alt="" /></a>
                           </section>

                        </div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <a href="#" class="image featured"><img src="resources/output/num02.jpg" alt="" /></a>
                           </section>

                        </div>
                     </div><br/>
                     <div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <img src="resources/output/arrow.png" alt="" /></br>
                              <img src="resources/output/tab.JPG" alt="" />
                           </section>
                        </div>

                     </div>


                     <h3>[ 차량 번호 인식 결과 ]</h3>
                     <p>추가로 한글을 학습시킨 TESSEARCT OCR로 </br>
                        이미지 전처리 작업을 마친 번호판 사진을 인식하여 차량 번호를 결과로 반환한다.</p>
                     <div class="row">
                        <div class="col-6 col-12-narrower">

                           <section>
                              <img src="resources/output/result01.JPG" alt="" />
                           </section>

                        </div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <img src="resources/output/result02.JPG" alt="" />
                           </section>
                        </div>
                     </div><br/><br/>
                     
                  


                     <footer class="major">
                        <ul class="buttons">
                           <li><a href="/testResult" class="button">결과 확인</a></li>
                        </ul>
                     </footer>

                  </section>

            </article>

         <!-- CTA -->
            <section id="cta">

               <header>
                  <h2>한양대학교 프로젝트 주도형 빅데이터 전문가 양성과정 </br>산학프로젝트 A-2조<strong>VIGILANTV</strong></h2>
                  <p>김지성 양주영 이새몬 이지현 최재영</p>
               </header>
               <footer>
                  <ul class="buttons">
                     <li><a href="#" class="button primary">문의하기</a></li>
                     <li><a href="#" class="button">맨 위로</a></li>
                  </ul>
               </footer>

            </section>

         <!-- Footer -->
            <footer id="footer">

               <ul class="icons">
                  <li><a href="#" class="icon circle fa-twitter"><span class="label">Twitter</span></a></li>
                  <li><a href="#" class="icon circle fa-facebook"><span class="label">Facebook</span></a></li>
                  <li><a href="#" class="icon circle fa-google-plus"><span class="label">Google+</span></a></li>
                  <li><a href="#" class="icon circle fa-github"><span class="label">Github</span></a></li>
                  <li><a href="#" class="icon circle fa-dribbble"><span class="label">Dribbble</span></a></li>
               </ul>

               <ul class="copyright">
                  <li>&copy; VIGILANTV</li><li>Design by y</li>
               </ul>

            </footer>

      </div>

      <!-- Scripts -->
         <script src="resources/assets/js/jquery.min.js"></script>
         <script src="resources/assets/js/jquery.dropotron.min.js"></script>
         <script src="resources/assets/js/jquery.scrolly.min.js"></script>
         <script src="resources/assets/js/jquery.scrollex.min.js"></script>
         <script src="resources/assets/js/browser.min.js"></script>
         <script src="resources/assets/js/breakpoints.min.js"></script>
         <script src="resources/assets/js/util.js"></script>
         <script src="resources/assets/js/main.js"></script>

   </body>
</html>