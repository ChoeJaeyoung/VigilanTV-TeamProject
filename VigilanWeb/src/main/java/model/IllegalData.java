package model;


public class IllegalData {
	private String plate_num;
	private String date_detect;
	private String time_detect;
	
	public IllegalData() {
		super();
	}

	public IllegalData(String plate_num, String date_detect, String time_detect) {
		super();
		this.plate_num = plate_num;
		this.date_detect = date_detect;
		this.time_detect = time_detect;
	}
	
	public String getPlate_num() {
		return plate_num;
	}
	public void setPlate_num(String plate_num) {
		this.plate_num = plate_num;
	}
	public String getDate_detect() {
		return date_detect;
	}
	public void setDate_detect(String date_detect) {
		this.date_detect = date_detect;
	}
	public String getTime_detect() {
		return time_detect;
	}
	public void setTime_detect(String time_detect) {
		this.time_detect = time_detect;
	}

	@Override
	public String toString() {
		return "IllegalData [plate_num=" + plate_num + ", date_detect=" + date_detect + ", time_detect=" + time_detect
				+ "]";
	}	

}
