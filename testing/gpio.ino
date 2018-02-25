

const int smoothing = 500;
const int sampleRate = 1;
const int threshold = 200;

void setup() {
 
  Serial.begin(9600);
  
 
} 
 
void loop() {
Process p; 
 int sum = 0;
  for(int i = 0; i<smoothing; i++){
    int sensorValue = analogRead(A0);
    sum += sensorValue;
    delay(sampleRate);
  }

  float average = sum/smoothing;

  if(average>=threshold){
	Serial.println("email");
	delay(10000);
  }
 
}
