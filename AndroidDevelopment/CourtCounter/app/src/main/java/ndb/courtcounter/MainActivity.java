package ndb.courtcounter;


import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity
{
    int scoreTeamA = 0;
    int scoreTeamB = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void displayScoreTeamA()
    {
        TextView scoreTeamATextView = (TextView)findViewById(R.id.score_team_A);
        scoreTeamATextView.setText("" + scoreTeamA);
    }

    public void displayScoreTeamB()
    {
        TextView scoreTeamATextView = (TextView)findViewById(R.id.score_team_B);
        scoreTeamATextView.setText("" + scoreTeamB);
    }

    public void increaseFreeThrowTeamA(View view)
    {
        ++scoreTeamA;
        displayScoreTeamA();
    }

    public void increaseTwoPointTeamA(View view)
    {
        scoreTeamA += 2;
        displayScoreTeamA();
    }

    public void increaseThreePointTeamA(View view)
    {
        scoreTeamA += 3;
        displayScoreTeamA();
    }

    public void increaseFreeThrowTeamB(View view)
    {
        ++scoreTeamB;
        displayScoreTeamB();
    }

    public void increaseTwoPointTeamB(View view)
    {
        scoreTeamB += 2;
        displayScoreTeamB();
    }

    public void increaseThreePointTeamB(View view)
    {
        scoreTeamB += 3;
        displayScoreTeamB();
    }

    public void resetScores(View view)
    {
        scoreTeamA = 0;
        scoreTeamB = 0;
        displayScoreTeamA();
        displayScoreTeamB();
    }
}
