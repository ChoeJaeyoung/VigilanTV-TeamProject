package kr.co.vigilan;

import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;
import java.util.Locale;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;

import com.google.gson.Gson;

import DAO.HiveConnect;
import model.CarCheck;
import model.IllegalData;

/**
 * Handles requests for the application home page.
 */
@Controller
public class HomeController {
	
	private static final Logger logger = LoggerFactory.getLogger(HomeController.class);
	
	/**
	 * Simply selects the home view to render by returning its name.
	 */
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String home(Locale locale, Model model) {
		logger.info("Welcome home! The client locale is {}.", locale);
		
		Date date = new Date();
		DateFormat dateFormat = DateFormat.getDateTimeInstance(DateFormat.LONG, DateFormat.LONG, locale);
		
		String formattedDate = dateFormat.format(date);
		
		model.addAttribute("serverTime", formattedDate );
		
		return "index";
	}
	
	@RequestMapping(value = "/carcheck")
	public String carCheck() {
		return "/carcheck";
	}
	
	@RequestMapping(value = "/index")
	public String index() {
		return "/index";
	}
	
	@RequestMapping(value = "/fileUpload")
	   public String fileUpload(HttpServletRequest req, Model model) {
	      System.out.println("fileUpload!!!!");
	      String path = "C:/Users/dlwlg/Desktop/demon/";
	      
	      try {
	      MultipartHttpServletRequest mhsr = (MultipartHttpServletRequest) req;
	      Iterator iter = mhsr.getFileNames();
	      
	      MultipartFile mfile = null;
	      String fieldName = "";
	      List resultList = new ArrayList();
	      
	      // �뵒�젅�넗由ш� �뾾�떎硫� �깮�꽦
	      File dir = new File(path);
	      if (!dir.isDirectory()) { 
	         dir.mkdirs(); 
	      }
	      
	      while(iter.hasNext()) {
	         fieldName = iter.next().toString();
	         mfile = mhsr.getFile(fieldName);
	         String origName;
	         
	         origName = new String(mfile.getOriginalFilename().getBytes("8859_1"), "UTF-8");
	         
	         if("".equals(origName)) {
	            continue;
	         }
	         
	         //�뙆�씪 紐� 蹂�寃�
	         String ext = origName.substring(origName.lastIndexOf('.'));
	         
	         String saveFileName = getCurrentTime() + ext;
	         
	         //�꽕�젙�븳 path�뿉 �뙆�씪���옣
	         File serverFile = new File(path + File.separator + saveFileName);
	         System.out.println("serverFile : " + serverFile);
	         mfile.transferTo(serverFile);
	         
	         model.addAttribute("path", path);
	         model.addAttribute("saveFileName", saveFileName);
	         System.out.println("SAVE : " + path + saveFileName);
	         
	      }
	   }catch (Exception e) {
	      // TODO Auto-generated catch block
	      e.printStackTrace();
	   }
	      
	      return "/index";
	   }
	
	@RequestMapping(value = "/testResult")
	public String testResult(HttpServletRequest req, Model model) {
		return "/result";
	}
		
	
	public static String getCurrentTime() {
		SimpleDateFormat sdfDate = new SimpleDateFormat("yyyy-MM-dd-HH.mm.ss");
		Date now = new Date();
		String nowTime = sdfDate.format(now);
		return nowTime;
	}
	
	@ResponseBody
	@RequestMapping(value = "/testajax", method = RequestMethod.GET)
	public ArrayList<String> testAjax(HttpServletRequest request, HttpServletResponse response, Model model) throws ClassNotFoundException, SQLException{
		System.out.println("Success Connect");
		
		String connectionTime = request.getParameter("connectionTime");
		
		HiveConnect hive = new HiveConnect();
		ArrayList<IllegalData> hiveArray = hive.illegalAlarm(connectionTime);
		
		Gson gson = new Gson();
		ArrayList<String> listJson = new ArrayList<String>();
		int sizeNum = 0;
		if(hiveArray.size()>0) {
			if(hiveArray.size()<5) {
				sizeNum = hiveArray.size();
			}else {
				sizeNum = 5;
			}
			for(int i = 0; i < sizeNum; i++) {
				String strJSON = gson.toJson(hiveArray.get(i));
				System.out.println("String to JSON : " + strJSON);
				listJson.add(strJSON);
			}
		}
		
		return listJson;
	}
	
	@RequestMapping(value = "/checkCar")
	   public String carCheck(HttpServletRequest request, Model model) throws SQLException, UnsupportedEncodingException {
	      request.setCharacterEncoding("utf-8");
	      String platenum = request.getParameter("plateNum");
	      System.out.println("차 번호 : " + platenum);
	      
	      ArrayList<CarCheck> carList = new ArrayList<CarCheck>();
	      HiveConnect hive2 = new HiveConnect();
	      Gson gson2 = new Gson();
	      
         carList = hive2.carCheck2(platenum);
         ArrayList<String> jsonList = new ArrayList<String>();
         for(int i = 0; i <carList.size(); i++) {
            String strJSON = gson2.toJson(carList.get(i));
            System.out.println("String to JSON : " + strJSON);
            jsonList.add(strJSON);
            System.out.println("Json List : " + strJSON);
            model.addAttribute("carArr", jsonList);
         }
         return "carcheck2";
	      
	   }
	
	@RequestMapping(value= "/updateCar")
	public String updateCar(HttpServletRequest request) throws ClientProtocolException, IOException {
		String changeNum = request.getParameter("changeNum");
		String row_key = request.getParameter("row_key");
		
		CloseableHttpClient client = HttpClients.createDefault();
		HttpPost httpPost = new HttpPost("http://localhost:5000/updateCar");
		
		JSONObject json = new JSONObject();
		json.put("changeNum", changeNum);
		json.put("row_key", row_key);
		
		httpPost.addHeader("Content-type", "application/json; charset=utf-8");
		httpPost.setEntity(new StringEntity(json.toString(), "UTF-8"));
		System.out.println("json_tostring" + json.toString());
		
		//Response
		HttpResponse response = client.execute(httpPost);
		System.out.println("response_1");
		
		
		return "carcheck";
	}
	
}
