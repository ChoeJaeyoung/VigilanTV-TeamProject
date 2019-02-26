package DAO;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import org.apache.hive.jdbc.HiveDriver;

import com.google.gson.Gson;

import model.CarCheck;
import model.IllegalData;

public class HiveConnect {
	Connection conn;
	Statement stmt;
	ResultSet rs;
	
	private static String forname = "org.apache.hive.jdbc.HiveDriver";
	String URL = "jdbc:hive2://192.168.1.137:10000/default";
	String root = "root";
	String pw = "1234";
	
	public HiveConnect(){
		try {
			Class.forName(forname);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public ArrayList<IllegalData> illegalAlarm(String format_time) throws SQLException {
		/*SimpleDateFormat format = new SimpleDateFormat("yyyyMMdd");
	    String format_time = format.format(System.currentTimeMillis());*/
	    //String format_time = "20190219181124";
		System.out.println(format_time);
		
		conn = DriverManager.getConnection(URL,root,pw);
		stmt = conn.createStatement();
	    //String query = "SELECT * FROM car_data.car_data where date_detect = '" + format_time+"'";
	    String query = "SELECT * FROM car_data.car_data where "
	    		+ "(from_unixtime(unix_timestamp(concat(date_detect,time_detect), 'yyyyMMddhhmmss'))"
	    		+ "> from_unixtime(unix_timestamp('"+format_time+"', 'yyyyMMddhhmmss')))=TRUE";

		rs = stmt.executeQuery(query);
		ArrayList<IllegalData> illegal = new ArrayList<IllegalData>();
		while(rs.next()) {
			IllegalData illegalData = new IllegalData();
			illegalData.setPlate_num(rs.getString("plate_num"));
			illegalData.setDate_detect(rs.getString("date_detect"));
			illegalData.setTime_detect(rs.getString("time_detect"));
			System.out.println(rs.getString("plate_num"));
			System.out.println(rs.getString("date_detect"));
			System.out.println(rs.getString("time_detect"));
			illegal.add(illegalData);
		}
		return illegal;
	}
	
	public ArrayList<IllegalData> testAlarm() throws SQLException{
	
		conn = DriverManager.getConnection(URL,root,pw);
		stmt = conn.createStatement();
		String query = "SELECT * FROM car_data.car_data_test";

		rs = stmt.executeQuery(query);
		ArrayList<IllegalData> illegal = new ArrayList<IllegalData>();
		while(rs.next()) {
			IllegalData illegalData = new IllegalData();
			illegalData.setPlate_num(rs.getString(0));
			illegalData.setDate_detect(rs.getString(1));
			illegalData.setTime_detect(rs.getString(2));
			illegal.add(illegalData);
		}
		System.out.println(illegal);
		return illegal;
	}
	
	public CarCheck carCheck(String plateNum) throws SQLException {
		      CarCheck carcheck = new CarCheck();      
		      conn = DriverManager.getConnection(URL, root, pw);
		      stmt = conn.createStatement();
		      System.out.println("차량 번호 : "+ plateNum);
		      String query2 = "SELECT * from car_data.car_data where plate_num ='" + plateNum+"'";
		      
		      rs = stmt.executeQuery(query2);
		      while(rs.next()) {
		         carcheck.setDate_detect(rs.getString("date_detect"));
		         carcheck.setImage_detect(rs.getString("image_detect"));
		         carcheck.setImage_plate(rs.getString("image_plate"));
		         carcheck.setImage_start(rs.getString("image_start"));
		         carcheck.setPlate_num(rs.getString("plate_num"));
		         carcheck.setTime_detect(rs.getString("time_detect"));
		         carcheck.setColor(rs.getString("color"));
		      }
		      
		      return carcheck;
	}	
	
	
	public void changeNum(String changeNum) throws SQLException {
	      conn = DriverManager.getConnection(URL, root, pw);
	      stmt = conn.createStatement();
	      System.out.println("차량 번호 : "+ changeNum);
	      String query3 = "SELECT * from car_data.car_data where plate_num ='" + changeNum + "'";
	      
	      rs = stmt.executeQuery(query3);
	}	
	
	public ArrayList<CarCheck> carCheck2(String plateNum) throws SQLException {
	      ArrayList<CarCheck> carList = new ArrayList<CarCheck>();      
	      conn = DriverManager.getConnection(URL, root, pw);
	      stmt = conn.createStatement();
	      System.out.println("차량 번호 : "+ plateNum);
	      String query2 = "SELECT * from car_data.car_data where plate_num ='" + plateNum+"'";
	      
	      rs = stmt.executeQuery(query2);
	      while(rs.next()) {
	         CarCheck carcheck = new CarCheck();
	         carcheck.setRow_key(rs.getString("row_key"));
	         carcheck.setDate_start(rs.getString("date_start"));
	         carcheck.setTime_start(rs.getString("time_start"));
	         carcheck.setDate_detect(rs.getString("date_detect"));
	         carcheck.setTime_detect(rs.getString("time_detect"));
	         carcheck.setImage_detect(rs.getString("image_detect"));
	         carcheck.setImage_plate(rs.getString("image_plate"));
	         carcheck.setImage_start(rs.getString("image_start"));
	         carcheck.setPlate_num(rs.getString("plate_num"));
	         carcheck.setColor(rs.getString("color"));

	         
	         carList.add(carcheck);
	      }
	      
	      return carList;
	}
	
	
}
