<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@taglib uri="http://www.springframework.org/tags" prefix="spring"%> 
<%@ page import ="java.util.ArrayList" %>
<!DOCTYPE HTML>
<!--
   Twenty by HTML5 UP
   html5up.net | @ajlkn
   Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<% 
String capture_path = "/image/"+(String)request.getAttribute("capture_path");
String final_plate = "/image/"+(String)request.getAttribute("final_plate");
String saveEvidenceCrop = (String)request.getAttribute("saveEvidenceCrop");
String saveTrackerCrop = (String)request.getAttribute("saveTrackerCrop");
String txt = (String)request.getAttribute("txt");
String final_save = "/image/"+(String)request.getAttribute("final_save");
System.out.println(capture_path + final_save);

ArrayList<String> carArr = (ArrayList<String>)request.getAttribute("carArr");
String jsonPlate = (String)request.getAttribute("carNumber");
%>

<html>
   <head>
      <title>VIGILANTV</title>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
      <link rel="stylesheet" href="resources/assets/css/main.css" />
      <noscript><link rel="stylesheet" href="resources/assets/css/noscript.css" /></noscript>
      <style>
      #file { width:0; height:0; }
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
		@font-face {
	        font-family: webisfree;
	        src: url('resources/output/KakaoRegular.ttf');
	    }
	      
	    body {
	        font-family: webisfree;
	    }
		
      </style>
      <meta charset="UTF-8">
      <script type="text/javascript">
      function openTextFile() {
         var input = document.createElement("input");

          input.type = "file";
                input.accept = "text/plain";

               input.onchange = function (event) {
                  processFile(event.target.files[0]);
             };
                input.click();
            }

            function processFile(file) {
               var reader = new FileReader();

               reader.onload = function () {
                  output.innerText = reader.result;
               };

               reader.readAsText(file, /* optional */ "euc-kr");
            }
        </script>

   </head>
   <body class="index is-preload">
      <div id="page-wrapper">

         <!-- Header -->
            <header id="header" class="alt">
               <h1 id="logo"><a href="index">VIGILANTV <span>by 2조</span></a></h1>
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
                  <p>
                  <strong>검색 결과<strong/>
                  <br />
                  </p>
                  <footer>
                     <ul class="buttons stacked">
                        <li><a href="#main" class="button fit scrolly">확인하기</a></li>
                     </ul>
                  </footer>

               </div>

            </section>

         <!-- Main -->
            <article id="main">

               <header class="special container">
                  <span class="icon fa-bar-chart-o"></span>
                  <h2><strong>불법 주·정차 차량 정보</strong></h2>
               </header>



               <!-- Three -->

                   <section class="wrapper style3 container special">
					 <script>
							var car = <%= jsonPlate %>;
							var carArr = <%= carArr %>;
							console.log(carArr);
							var sample_jsoncar = JSON.stringify(carArr[0]);
							var sample_car = JSON.parse(sample_jsoncar);
							
							document.write("<h2>차량 번호 : " + sample_car.plate_num + "</h2>");
							document.write("<ul>");
							for(var i=0; i<carArr.length; i++) {
								var jsoncar = JSON.stringify(carArr[i]);
								var car = JSON.parse(jsoncar);
								var date = car.date_detect;
								var year = date.substring(0,4);
								var month = date.substring(4,6);
								var day = date.substring(6,8);
								var time = car.time_detect;
																
								var addDate = new Date(year, month, day);
								addDate.setDate(addDate.getDate() + 33);
								
								var hour = time.substring(0,2);
								var min = time.substring(2,4);
								var sec = time.substring(4,6);
								
								document.write("<li><a href='#" + i + "'>" + year + "년 " + month + "월 " + day + "일  (" + hour + "시 " + min + "분 " + sec + "초" + ")</a></li>");
							}
							document.write("</ul>");
							
							for(var i=0; i<carArr.length; i++) {
								var jsoncar = JSON.stringify(carArr[i]);
								var car = JSON.parse(jsoncar)
								var rowkey = car.row_key;
								
								document.write("<table class='type09' id='" + i + "'>");
						        document.write("<thead>");
								document.write("<tr><th scope='cols'></th><th scope='cols'></th></tr>");
								document.write("</thead>");
								document.write("<tbody>");
								document.write("<tr>");
								document.write("<th scope='row'>"+"차량 번호"+"</th>");
								document.write("<td>" + "<form action='updateCar'>");
								document.write("<input name='row_key' type='hidden' value = " + rowkey + ">");
								document.write("<input name='changeNum' type='text' style='width:200px; display:inline;' value='" + car.plate_num + "'><input type='submit' style='width:50px;' value='수정'>");
								document.write("</form></td>");
								document.write("</tr>");
								document.write("<tr>");
								document.write("<th scope='row'>"+"차량 색상"+"</th>");
								document.write("<td text-align='center'>"+ car.color + "</td>");
								document.write("</tr>");
								document.write("<tr>");
								document.write("<th scope='row'>"+"위반 일시"+"</th>");
								document.write("<td text-align='center'>" + year + "년 " + month + "월 " + day + "일 - " + hour + "시 " + min + "분 " + sec + "초" + "</td>");
						        document.write("</tr>");
						        document.write("<tr>");
						        document.write("<th scope='row'>"+"위반 내용"+"</th>");
								document.write("<td text-align='center'>주정차금지구역</td>");
						        document.write("</tr>");
						        document.write("<tr>");
						        document.write("<th scope='row'>자진납부 및 의견진술 기한</th>");
								document.write("<td>" + addDate.getFullYear() + "년 " + addDate.getMonth() + "월 " + addDate.getDate() + "일" + "까지입니다.<br/><br/><font color=red><font color=blue>※의견진술 기한내 자진납부시 <font color=red>20%</font> 경감적용 </font> 수용이 되지 않을 경우 감경되지 않고 본 과태료 부과 됨</font></td>");
						        document.write("</tr>");
						        document.write("<tr>");
						        document.write("<th scope='row'>"+"단속 구분"+"</th>");
								document.write("<td text-align='center'>고정형 CCTV</td>");
						        document.write("</tr>");
						        
						        document.write("<tr>");
						        document.write("<th scope='row'>"+"증거사진"+"</th>");
								document.write("<td text-align='center'>");
								document.write("<img src='http://192.168.1.67:50070/webhdfs/v1/car-detection/nifi-collect/" + car.image_start + "?op=OPEN' style='max-width: 50%; height: auto;'>");
								document.write("<img src='http://192.168.1.67:50070/webhdfs/v1/car-detection/nifi-collect/" + car.image_detect + "?op=OPEN' style='max-width: 50%; height: auto;'>");
								document.write("<img src='http://192.168.1.67:50070/webhdfs/v1/car-detection/nifi-collect/" + car.image_plate + "?op=OPEN' style='max-width: 50%; height: auto;'>");
								document.write("</td>");
						        document.write("</tr>");
						        
						        
						        document.write("</tbody>");
						        document.write("</table>");
							}
							
						
					        
					</script>

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