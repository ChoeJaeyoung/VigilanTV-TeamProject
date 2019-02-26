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
String carColor = (String)request.getAttribute("carColor");
String time = (String)request.getAttribute("time");

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
               <h1 id="logo"><a href="/">VIGILANTV <span>by 2조</span></a></h1>
               <nav id="nav">
                  <ul>
                     <li class="current"><a href="index.html">Welcome</a></li>
                     <li class="submenu">
                        <a href="#">Layouts</a>
                        <ul>
                           <li><a href="left-sidebar.html">Left Sidebar</a></li>
                           <li><a href="right-sidebar.html">Right Sidebar</a></li>
                           <li><a href="no-sidebar.html">No Sidebar</a></li>
                           <li><a href="contact.html">Contact</a></li>
                           <li class="submenu">
                              <a href="#">Submenu</a>
                              <ul>
                                 <li><a href="#">Dolore Sed</a></li>
                                 <li><a href="#">Consequat</a></li>
                                 <li><a href="#">Lorem Magna</a></li>
                                 <li><a href="#">Sed Magna</a></li>
                                 <li><a href="#">Ipsum Nisl</a></li>
                              </ul>
                           </li>
                        </ul>
                     </li>
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
                  <h2><strong>분석 결과</strong></h2>
               </header>



               <!-- Three -->

                   <section class="wrapper style3 container special">
                     <header>
                        <h2>어린이 보호 구역 <strong>불법 주·정차 차량</strong>정보</h2>
                     </header><br/>

                     <div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <header>
                                 <h3>증거 사진</h3>
                                 <p></p>
                              </header>
                              <a href="#" class="image featured"><img src="<spring:url value='<%=capture_path+saveEvidenceCrop %>'/>" alt="" /></a>
                              <header>
                                 <h3></h3>
                              </header>

                           </section>

                        </div>
                     </div>


                     <div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <a href="#" class="image featured"><img src="<spring:url value='<%=capture_path+saveTrackerCrop %>'/>" alt="" /></a>
                              <header>
                                 <h3></h3>
                              </header>

                           </section>

                        </div>
                     </div>


                     <div>
                        <div class="col-6 col-12-narrower">

                           <section>
                              <header>
                                 <h3>차량 번호판 사진</h3>
                              </header>
                              <a href="#"><img src="<spring:url value='<%=final_plate%>'/>" alt="" /></a></br></br></br>
                              <a href="#"><img src="<spring:url value='<%=final_save%>'/>" alt="" /></a>
                              <header>
                                 <h3></h3>
                              </header>
                           </section>

                        </div>
                     </div>
                     <br/><br/>
                     
                    <input type="hidden" id="video" value=""/> <!-- 파일명 확인용 -->
					<video id="videoPlay" width="700" height="600" controls autoplay>       
					    <source type="video/mp4" src="" type="video/mp4" />       
					    <source src="<spring:url value='<%=capture_path%>'/>output.mp4" type="video/mp4">       
					    Your browser does not support HTML5 video.    
					</video>
                     
                     <button onclick="openTextFile()">차량번호</button><br/><br/><br/>
                     <div id='output'>
						<h1>차량 번호 : ${txt}</h1><br/>
                     </div>
                     <div>
                     	<h1>차량 색상 : ${carColor}</h1>
                     </div>
                     <div>
                     	<h1>불법  주·정차 시작 시각 : ${time}</h1>
                     </div>

                  </section>

            </article>

         <!-- CTA -->
            <section id="cta">

               <header>
                  <h2>Ready to do <strong>something</strong>?</h2>
                  <p>Proin a ullamcorper elit, et sagittis turpis integer ut fermentum.</p>
               </header>
               <footer>
                  <ul class="buttons">
                     <li><a href="#" class="button primary">Take My Money</a></li>
                     <li><a href="#" class="button">LOL Wut</a></li>
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