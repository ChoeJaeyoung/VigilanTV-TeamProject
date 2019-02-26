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
                     <li><a href="#" class="button primary">조회하기</a></li>
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
                  <h2><strong>불법 주·정차 차량 정보 조회</strong></h2>
               </header>



               <!-- Three -->

                   <section class="wrapper style3 container special">
                   <%= jsonPlate %>
                     
					</br></br></br>
					 <script>
							var car = <%= jsonPlate %>;
							var json = JSON.stringify(car);
						
							var car2 = JSON.parse(json);
					        document.write("<table class='type09'>");
					        document.write("<thead>");
					        document.write("<tr scope='rows' bgcolor='#F6F6F6'>");
							document.write("<th scope='rows' class='carnum'>"+"차량번호"+"</th>");
					        document.write("<th scope='rows' class='carnum'>"+"차량색상"+"</th>");
					        document.write("<th scope='rows' class='carnum'>"+"시작시각"+"</th>");
					        document.write("</tr>");
					        document.write("</thead>");
					        document.write("<tbody>");
					        document.write("<tr scope='rows' bgcolor='white'>");
					        document.write("<td text-align='center'>"+ car2.plate_num + "</td>");
					        document.write("<td text-align='center'>"+ car2.color + "</td>");
					        document.write("<td text-align='center'>"+ car2.date_detect + car2.time_detect + "</td>");
							document.write("</tr>");
					        document.write("</tbody>");
					        document.write("</table>");
					</script>
					
					

					    <div>
					      <section>
					        <header>
							  <table class="type09">
								<thead>
								<tr>
									<th scope="cols"></th>
									<th scope="cols"></th>
								</tr>
								</thead>
								<tbody>
								<tr>
									<th scope="row">차량 번호</th>
									<td>12가 1234</td>
								</tr>
								<tr>
									<th scope="row">위반 일시</th>
									<td>2019-02-13 17:07:09</td>
								</tr>
								<tr>
									<th scope="row">위반 내용</th>
									<td>주정차금지구역</td>
								</tr>
								<tr>
									<th scope="row">자진납부 및 의견진술 기한</th>
									<td>2019-03-18 까지입니다.<br/><font color=red><font color=blue>※의견진술 기한내 자진납부시 <font color=red>20%</font> 경감적용 </font> 수용이 되지 않을 경우 감경되지 않고 본 과태료 부과 됨</font></td>
								</tr>
								<tr>
									<th scope="row">단속 구분</th>
									<td>고정형 CCTV</td>
								</tr>
								</tbody>
							  </table>
						    </header>
					      </section>
				        </div>

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


                     <div>
                           <section>
                              <a href="#" class="image featured"><img src="<spring:url value='<%=capture_path+saveTrackerCrop %>'/>" alt="" /></a>
                              <header>
                                 <h3></h3>
                              </header>
                           </section>
                     </div>
                     <div>
                           <section>
                              <a href="#"><img src="<spring:url value='<%=final_plate%>'/>" alt="" /></a>
                              <header>
                                 <h3></h3>
                              </header>
                           </section>
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