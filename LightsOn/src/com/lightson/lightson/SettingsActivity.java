package com.lightson.lightson;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;

public class SettingsActivity extends Activity {

	public static boolean isGame4 = true;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.settings);
	}
	
	public void setGame(View view){
		switch(view.getId()){
		case R.id.choose4: 	isGame4 = true;		break;
		case R.id.choose8: 	isGame4 = false;	break;
		default:			isGame4 = true;		break;
		}
	}
}
