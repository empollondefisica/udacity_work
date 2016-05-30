
package ndb.testapp;


import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

import java.io.File;

public class MainActivity extends AppCompatActivity
{
    private Toolbar  cToolbar;
    private LinearLayout cLinearLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        cToolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(cToolbar);

        cLinearLayout = (LinearLayout)findViewById(R.id.content_layout);

        buildFileView(new File("/"), cLinearLayout);
    }

    @Override
    public void onBackPressed()
    {
        buildFileView(new File("/"), cLinearLayout);
    }

    private void buildFileView(File pFile, LinearLayout pLinearLayout)
    {
        if(pFile.isDirectory())
        {
            pLinearLayout.removeAllViews();

            File[]        vFiles         = pFile.listFiles();
            StringBuilder vStringBuilder = new StringBuilder();

            if(vFiles != null)
            {
                for(File vFile : vFiles)
                {
                    Button vButton = new Button(getApplicationContext());

                    vStringBuilder.append(pFile.getAbsoluteFile());
                    if(!pFile.getAbsolutePath().equals("/"))
                    {
                        vStringBuilder.append("/");
                    }
                    vStringBuilder.append(vFile.getName());

                    vButton.setText(vStringBuilder.toString());
                    vButton.setOnClickListener(buildFileClickListener(vFile, pLinearLayout));

                    pLinearLayout.addView(vButton);

                    vStringBuilder.setLength(0);
                }
            }
        }
    }

    private View.OnClickListener buildFileClickListener(final File pFile, final LinearLayout pLinearLayout)
    {
        return new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                if(pFile.isDirectory())
                {
                    buildFileView(pFile, pLinearLayout);
                }
            }
        };
    }
}
