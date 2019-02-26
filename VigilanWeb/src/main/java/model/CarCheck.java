package model;

public class CarCheck {
	
	private String row_key;
	private String date_start;
	private String time_start;
	private String date_detect;
	private String time_detect;
	private String color;
	private String plate_num;
	private String image_start;
	private String image_detect;
	private String image_plate;
	
	public CarCheck() {
		super();
	}

	
	
	public CarCheck(String plate_num, String date_detect, String time_detect, String image_plate, String image_start,
			String image_detect, String color) {
		super();
		this.plate_num = plate_num;
		this.date_detect = date_detect;
		this.time_detect = time_detect;
		this.image_plate = image_plate;
		this.image_start = image_start;
		this.image_detect = image_detect;
		this.color = color;
	}



	public String getColor() {
		return color;
	}




	public CarCheck(String row_key, String date_start, String time_start, String date_detect, String time_detect,
			String color, String plate_num, String image_start, String image_detect, String image_plate) {
		super();
		this.row_key = row_key;
		this.date_start = date_start;
		this.time_start = time_start;
		this.date_detect = date_detect;
		this.time_detect = time_detect;
		this.color = color;
		this.plate_num = plate_num;
		this.image_start = image_start;
		this.image_detect = image_detect;
		this.image_plate = image_plate;
	}



	public String getDate_start() {
		return date_start;
	}



	public void setDate_start(String date_start) {
		this.date_start = date_start;
	}



	public String getTime_start() {
		return time_start;
	}



	public void setTime_start(String time_start) {
		this.time_start = time_start;
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



	public String getPlate_num() {
		return plate_num;
	}



	public void setPlate_num(String plate_num) {
		this.plate_num = plate_num;
	}



	public String getImage_start() {
		return image_start;
	}



	public void setImage_start(String image_start) {
		this.image_start = image_start;
	}



	public String getImage_detect() {
		return image_detect;
	}



	public void setImage_detect(String image_detect) {
		this.image_detect = image_detect;
	}



	public String getImage_plate() {
		return image_plate;
	}



	public void setImage_plate(String image_plate) {
		this.image_plate = image_plate;
	}



	public void setColor(String color) {
		this.color = color;
	}



	public String getRow_key() {
		return row_key;
	}



	public void setRow_key(String row_key) {
		this.row_key = row_key;
	}
	
	
	
}
