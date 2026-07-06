// Controlling a simple to build robot arm
// For details see: https://homofaciens.de/technics-machines-robot-arm-v1-0_en.htm

#include <Servo.h>

// Joint A = Rotation of arm
// Joint B = UP / DOWN of arm
// Joint C = Forward / Backward of arm
// Joint D = Rotaion of gripper
// Joint E = Gripper

#define STEPPER_ENABLE    8

#define JOINT_A_DIR       5
#define JOINT_A_STEP      2

#define JOINT_B_DIR       6
#define JOINT_B_STEP      3

#define JOINT_C_DIR       7
#define JOINT_C_STEP      4

#define GRIPPER_SERVO    12
#define ANGLE_SERVO      13
#define ANGLE_SERVO_DEFAULT  80

#define COMMAND_PAUSE     5
#define STEP_PAUSE       70

Servo gripperServo;
Servo angleServo;

#define READ_MAX 50
char serialBuffer[READ_MAX];
int readNumber;

#define JOINT_A_MAX   50000
#define JOINT_A_MIN  -50000
long joint_a, joint_a_old;

#define JOINT_B_MAX   50000
#define JOINT_B_MIN  -50000
long joint_b, joint_b_old;

#define JOINT_C_MAX   50000
#define JOINT_C_MIN  -50000
long joint_c, joint_c_old;

#define JOINT_D_MAX    180
#define JOINT_D_MIN      0
long joint_d, joint_d_old;

#define JOINT_E_MAX    180
#define JOINT_E_MIN      0
long joint_e, joint_e_old;

long extractInt(char c1, char c2, int mode){
  long number = 0;
  long sign = 1;
  char startConversion = 0;
  for(int i = 0; i < READ_MAX; i++){
    if(startConversion == 1){
      if(serialBuffer[i] >= '0' && serialBuffer[i] <= '9'){
        number = number * 10L;
        number += (serialBuffer[i] - '0');
      }
      else{
        if(serialBuffer[i] == '-'){
          sign = -1;
        }
        if(serialBuffer[i] != ' ' && serialBuffer[i] != '-'){
          return number * sign;
        }
      }
    }
    if(serialBuffer[i] == c1 && serialBuffer[i+1] == c2){
      if(mode == 0){
        return i;
      }
      startConversion = 1;
      i = i + 1;
    }
    if(serialBuffer[i]=='\0'){
      return -1;
    }
  }
  //Serial.println(number);
  return number * sign;
}

long moveJoint(){
  long moveMax = 0;
  double moveFraction_a = 0.0;
  double moveFraction_b = 0.0;
  double moveFraction_c = 0.0;
  double moveFraction_d = 0.0;
  double moveFraction_e = 0.0;
  double doMove_a = 0.0;
  double doMove_b = 0.0;
  double doMove_c = 0.0;
  double doMove_d = 0.0;
  double doMove_e = 0.0;
  int stepAdd_a = 1;
  int stepAdd_b = 1;
  int stepAdd_c = 1;
  int stepAdd_d = 1;
  int stepAdd_e = 1;

  if(moveMax < abs(joint_a - joint_a_old)) moveMax = abs(joint_a - joint_a_old);
  if(moveMax < abs(joint_b - joint_b_old)) moveMax = abs(joint_b - joint_b_old);
  if(moveMax < abs(joint_c - joint_c_old)) moveMax = abs(joint_c - joint_c_old);
  if(moveMax < abs(joint_d - joint_d_old)) moveMax = abs(joint_d - joint_d_old);
  if(moveMax < abs(joint_e - joint_e_old)) moveMax = abs(joint_e - joint_e_old);

  if(moveMax == 0) return -1;

  moveFraction_a = (double)(abs(joint_a - joint_a_old)) / (double)(moveMax);
  moveFraction_b = (double)(abs(joint_b - joint_b_old)) / (double)(moveMax);
  moveFraction_c = (double)(abs(joint_c - joint_c_old)) / (double)(moveMax);
  moveFraction_d = (double)(abs(joint_d - joint_d_old)) / (double)(moveMax);
  moveFraction_e = (double)(abs(joint_e - joint_e_old)) / (double)(moveMax);

  if(joint_a > joint_a_old){
    digitalWrite(JOINT_A_DIR, 1);
  }
  else{
    digitalWrite(JOINT_A_DIR, 0);
    stepAdd_a = -1;
  }

  if(joint_b > joint_b_old){
    digitalWrite(JOINT_B_DIR, 1);
  }
  else{
    digitalWrite(JOINT_B_DIR, 0);
    stepAdd_b = -1;
  }

  if(joint_c > joint_c_old){
    digitalWrite(JOINT_C_DIR, 1);
  }
  else{
    digitalWrite(JOINT_C_DIR, 0);
    stepAdd_c = -1;
  }

  if(joint_d < joint_d_old){
    stepAdd_d = -1;
  }

  if(joint_e < joint_e_old){
    stepAdd_e = -1;
  }


  for(long i = 0; i < moveMax; i++){
    doMove_a += moveFraction_a;
    doMove_b += moveFraction_b;
    doMove_c += moveFraction_c;
    doMove_d += moveFraction_d;
    doMove_e += moveFraction_e;

    if(doMove_a >= 1.0){
      digitalWrite(JOINT_A_STEP, 1);
      doMove_a -= 1.0;
      joint_a_old += stepAdd_a;
    }

    if(doMove_b >= 1.0){
      digitalWrite(JOINT_B_STEP, 1);
      doMove_b -= 1.0;
      joint_b_old += stepAdd_b;
    }

    if(doMove_c >= 1.0){
      digitalWrite(JOINT_C_STEP, 1);
      doMove_c -= 1.0;
      joint_c_old += stepAdd_c;
    }

    if(doMove_d >= 1.0){
      joint_d_old += stepAdd_d;
      angleServo.write(joint_d_old);
      doMove_d -= 1.0;
    }

    if(doMove_e >= 1.0){
      joint_e_old += stepAdd_e;
      gripperServo.write(joint_e_old  );
      doMove_e -= 1.0;
    }

    delayMicroseconds(COMMAND_PAUSE);
    digitalWrite(JOINT_A_STEP, 0);
    digitalWrite(JOINT_B_STEP, 0);
    digitalWrite(JOINT_C_STEP, 0);
    delayMicroseconds(STEP_PAUSE);
  }

  // Make missing steps due to rounding errors
  digitalWrite(JOINT_A_DIR, 1);
  while(joint_a_old < joint_a){
    digitalWrite(JOINT_A_STEP, 1);
    delayMicroseconds(COMMAND_PAUSE);
    digitalWrite(JOINT_A_STEP, 0);
    delayMicroseconds(STEP_PAUSE);
    joint_a_old ++;
  }

  digitalWrite(JOINT_A_DIR, 0);
  while(joint_a_old > joint_a){
    digitalWrite(JOINT_A_STEP, 1);
    delayMicroseconds(COMMAND_PAUSE);
    digitalWrite(JOINT_A_STEP, 0);
    delayMicroseconds(STEP_PAUSE);
    joint_a_old --;
  }

  digitalWrite(JOINT_B_DIR, 1);
  while(joint_b_old < joint_b){
    digitalWrite(JOINT_B_STEP, 1);
    delayMicroseconds(COMMAND_PAUSE);
    digitalWrite(JOINT_B_STEP, 0);
    delayMicroseconds(STEP_PAUSE);
    joint_b_old ++;
  }

  digitalWrite(JOINT_B_DIR, 0);
  while(joint_b_old > joint_b){
    digitalWrite(JOINT_B_STEP, 1);
    delayMicroseconds(COMMAND_PAUSE);
    digitalWrite(JOINT_B_STEP, 0);
    delayMicroseconds(STEP_PAUSE);
    joint_b_old --;
  }

  digitalWrite(JOINT_C_DIR, 1);
  while(joint_c_old < joint_c){
    digitalWrite(JOINT_C_STEP, 1);
    delayMicroseconds(COMMAND_PAUSE);
    digitalWrite(JOINT_C_STEP, 0);
    delayMicroseconds(STEP_PAUSE);
    joint_c_old ++;
  }

  digitalWrite(JOINT_C_DIR, 0);
  while(joint_c_old > joint_c){
    digitalWrite(JOINT_C_STEP, 1);
    delayMicroseconds(COMMAND_PAUSE);
    digitalWrite(JOINT_C_STEP, 0);
    delayMicroseconds(STEP_PAUSE);
    joint_c_old --;
  }

  angleServo.write(joint_d);
  joint_d_old = joint_d;
  gripperServo.write(joint_e);
  joint_e_old = joint_e;


  return 0;
}

void setup(){
  Serial.begin(115200);
  joint_a = 0; joint_a_old = 0;
  joint_b = 0; joint_b_old = 0;
  joint_c = 0; joint_c_old = 0;
  joint_d = ANGLE_SERVO_DEFAULT; joint_d_old = ANGLE_SERVO_DEFAULT;
  joint_e = 90; joint_e_old = 90;
  readNumber = 0;

  pinMode(JOINT_A_DIR, OUTPUT);
  pinMode(JOINT_A_STEP, OUTPUT);

  pinMode(JOINT_B_DIR, OUTPUT);
  pinMode(JOINT_B_STEP, OUTPUT);

  pinMode(JOINT_C_DIR, OUTPUT);
  pinMode(JOINT_C_STEP, OUTPUT);

  pinMode(STEPPER_ENABLE, OUTPUT);
  digitalWrite(STEPPER_ENABLE, 0);

  angleServo.attach(ANGLE_SERVO);  // attaches the servo on pin 9 to the servo object
  angleServo.write(joint_d);
  gripperServo.attach(GRIPPER_SERVO);  // attaches the servo on pin 9 to the servo object
  gripperServo.write(joint_e);
}

void loop(){

  if (Serial.available()) {  // If anything comes in Serial (USB),
    char readByte = Serial.read();
    //Serial.write(readByte);
    if(readNumber == READ_MAX - 1){
      readNumber = 0;
    }
    serialBuffer[readNumber] = readByte;
    serialBuffer[readNumber + 1]='\0';
    readNumber++;

    if(readByte == '\n' || readByte == 'N'){
      if(serialBuffer[0]=='E' && serialBuffer[1]=='N'){// ENABLE motors
        digitalWrite(STEPPER_ENABLE, 0);
        angleServo.attach(ANGLE_SERVO);
        angleServo.write(joint_d);
        gripperServo.attach(GRIPPER_SERVO);        
        gripperServo.write(joint_e);
      }
      if(serialBuffer[0]=='D' && serialBuffer[1]=='I' && serialBuffer[2]=='S'){// DISABLE motors
        digitalWrite(STEPPER_ENABLE, 1);
        angleServo.detach();
        gripperServo.detach();        
      }
      if(extractInt('Z', 'Z', 0) > -1){// Set coordinates to zero
        joint_a = 0; joint_a_old = 0;
        joint_b = 0; joint_b_old = 0;
        joint_c = 0; joint_c_old = 0;
        joint_d = ANGLE_SERVO_DEFAULT; joint_d_old = ANGLE_SERVO_DEFAULT;
        joint_e = 90; joint_e_old = 90;
      }

      if(extractInt('J', 'a', 0) > -1){// Absolute movement Joint 1 (ROTATE)
        joint_a = extractInt('J', 'a', 1);
        if(joint_a > JOINT_A_MAX) joint_a = JOINT_A_MAX;
        if(joint_a < JOINT_A_MIN) joint_a = JOINT_A_MIN;
      }
      if(extractInt('j', 'a', 0) > -1){// Relative movement Joint 2 (ROTATE)
        joint_a = joint_a + extractInt('j', 'a', 1);
        if(joint_a > JOINT_A_MAX) joint_a = JOINT_A_MAX;
        if(joint_a < JOINT_A_MIN) joint_a = JOINT_A_MIN;
      }

      if(extractInt('J', 'b', 0) > -1){// Absolute movement Joint 2 (UP/DOWN)
        joint_b = extractInt('J', 'b', 1);
        if(joint_b > JOINT_B_MAX) joint_b = JOINT_B_MAX;
        if(joint_b < JOINT_B_MIN) joint_b = JOINT_B_MIN;
      }
      if(extractInt('j', 'b', 0) > -1){// Relative movement Joint 2 (UP/DOWN)
        joint_b = joint_b + extractInt('j', 'b', 1);
        if(joint_b > JOINT_B_MAX) joint_b = JOINT_B_MAX;
        if(joint_b < JOINT_B_MIN) joint_b = JOINT_B_MIN;
      }

      if(extractInt('J', 'c', 0) > -1){// Absolute movement Joint 3 (BACK/FORWARD)
        joint_c = extractInt('J', 'c', 1);
        if(joint_c > JOINT_C_MAX) joint_c = JOINT_C_MAX;
        if(joint_c < JOINT_C_MIN) joint_c = JOINT_C_MIN;
      }
      if(extractInt('j', 'c', 0) > -1){// Relative movement Joint 3 (BACK/FORWARD)
        joint_c = joint_c + extractInt('j', 'c', 1);
        if(joint_c > JOINT_C_MAX) joint_c = JOINT_C_MAX;
        if(joint_c < JOINT_C_MIN) joint_c = JOINT_C_MIN;
      }

      if(extractInt('J', 'd', 0) > -1){// Absolute movement Joint 4 (Servo)
        joint_d = extractInt('J', 'd', 1);
        if(joint_d > JOINT_D_MAX) joint_d = JOINT_D_MAX;
        if(joint_d < JOINT_D_MIN) joint_d = JOINT_D_MIN;
      }
      if(extractInt('j', 'd', 0) > -1){// Relative movement Joint 4 (Servo)
        joint_d = joint_d + extractInt('j', 'd', 1);
        if(joint_d > JOINT_D_MAX) joint_d = JOINT_D_MAX;
        if(joint_d < JOINT_D_MIN) joint_d = JOINT_D_MIN;
      }

      if(extractInt('J', 'e', 0) > -1){// Absolute movement Gripper
        joint_e = extractInt('J', 'e', 1);
        if(joint_e > JOINT_E_MAX) joint_e = JOINT_E_MAX;
        if(joint_e < JOINT_E_MIN) joint_e = JOINT_E_MIN;
      }
      if(extractInt('j', 'e', 0) > -1){// Relative movement Gripper
        joint_e = joint_e + extractInt('j', 'e', 1);
        if(joint_e > JOINT_E_MAX) joint_e = JOINT_E_MAX;
        if(joint_e < JOINT_E_MIN) joint_e = JOINT_E_MIN;
      }

      moveJoint();
      Serial.print("Ja: "); Serial.print(joint_a);
      Serial.print(" Jb: "); Serial.print(joint_b);
      Serial.print(" Jc: "); Serial.print(joint_c);
      Serial.print(" Jd: "); Serial.print(joint_d);
      Serial.print(" Je: "); Serial.println(joint_e);

      readNumber = 0;
    }
  }

}
