package ndb.androidapp;


import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity
{

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        RelativeLayout vRelativeLayout = (RelativeLayout)findViewById(R.id.parent_layout);
        TextView vTextView = new TextView(getApplicationContext());

        vTextView.setText("FAVORITE");
        vTextView.setTextColor(Color.RED);
        vTextView.setTextSize(56);

        vTextView.getMaxLines();

        vRelativeLayout.addView(vTextView);


    }
}
