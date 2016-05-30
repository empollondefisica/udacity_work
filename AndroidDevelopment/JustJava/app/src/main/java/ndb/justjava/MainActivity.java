package ndb.justjava;


import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;

import java.text.NumberFormat;

public class MainActivity extends AppCompatActivity
{
    private int quantity = 0;
    private double price    = 5;

    CheckBox whippedCheckBox;
    CheckBox chocolateCheckBox;
    EditText nameEditText;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        nameEditText = (EditText)findViewById(R.id.name_text_view);
        whippedCheckBox = (CheckBox)findViewById(R.id.whipped_cream);
        chocolateCheckBox = (CheckBox)findViewById(R.id.chocolate);
    }

    private void display(int number)
    {
        TextView quantityTextView = (TextView) findViewById( R.id.quantity_text_view);
        quantityTextView.setText("" + number);
    }

    private void displayPrice(double number)
    {
        TextView priceTextView = (TextView) findViewById(R.id.price_text_view);
        StringBuilder vValue = new StringBuilder();

        vValue.append("Name: ");
        vValue.append(nameEditText.getText().toString());
        vValue.append("\n");

        if(whippedCheckBox.isChecked())
        {
            vValue.append("Add Whipped Cream\n");
        }

        if(chocolateCheckBox.isChecked())
        {
            vValue.append("Add Chocolate\n");
        }

        vValue.append("Quantity: ");
        vValue.append(quantity);
        vValue.append("\n");
        vValue.append("Total: ");
        vValue.append(NumberFormat.getCurrencyInstance().format(number));
        vValue.append("\nThank you!");

        priceTextView.setText(vValue.toString());

        Intent vIntent = new Intent(Intent.ACTION_SENDTO);
        vIntent.setData(Uri.parse("mailto:"));
        vIntent.putExtra(Intent.EXTRA_SUBJECT, "Just Java Order for " + nameEditText.getText().toString());
        vIntent.putExtra(Intent.EXTRA_TEXT, vValue.toString());
        if(vIntent.resolveActivity(getPackageManager()) != null)
        {
            startActivity(vIntent);
        }


    }

    public void submitOrder(View view)
    {
        double total = quantity * price;

        if(whippedCheckBox.isChecked())
        {
            total += (quantity * 0.50);
        }

        if(chocolateCheckBox.isChecked())
        {
            total += (quantity * 1.00);
        }

        display(quantity);
        displayPrice(total);
    }

    public void increaseQuantity(View view)
    {
        display(++quantity);
    }

    public void decreaseQuantity(View view)
    {
        if(quantity > 0)
        {
            display(--quantity);
        }
    }
}
