<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@taglib uri="http://www.springframework.org/tags" prefix="spring"%> 
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
                  <strong>불법 주·정차 차량 정보 조회<strong/>
                  <br />
                  </p>
                  <footer>
                     <ul class="buttons stacked">
                        <li><a href="#main" class="button fit scrolly">조회하기</a></li>
                     </ul>
                  </footer>

               </div>

            </section>

         <!-- Main -->
            <article id="main">

               <header class="special container">
                  <span class="icon fa-bar-chart-o"></span>
                  <h2><strong>불법 주·정차 차량 정보 조회</strong></h2>
               </header>



               <!-- Three -->

                   <section class="wrapper style3 container special">
                     <form class="text", action="checkCar">
						<input type="text" name="plateNum" placeholder="조회할 차량 번호를 입력해주세요.">
					</form>
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