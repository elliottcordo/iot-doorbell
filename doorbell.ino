
int button = D0;
int led = D7;

void setup() {
    Serial.begin(9600);
    pinMode(button, INPUT_PULLDOWN);
    pinMode(led, OUTPUT);
    
    digitalWrite(led, HIGH);
    delay(2000);
    digitalWrite(led, LOW);
    delay(2000);
    digitalWrite(led, HIGH);
    delay(2000);
    digitalWrite(led, LOW);
}

void loop() {
    int currState = digitalRead(button);
    
    if (currState == 1) {
        Serial.println("button pressed!");
        Spark.publish("doorbell","pressed",600,PRIVATE);
        digitalWrite(led, HIGH);
        delay(5000);
        digitalWrite(led, LOW);
    }
}
