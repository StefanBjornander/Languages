import React, {useState} from 'react';
import auth from '@react-native-firebase/auth';
import {
  Text,
  TextInput,
  View,
  KeyboardAvoidingView,
  TouchableOpacity,
  Image,
} from 'react-native';
import styles from '../settings/Styles';

const LoginScreen = () => {
  const [phoneNumber, setPhoneNumber] = useState('');
  // If null, no SMS has been sent
  const [confirm, setConfirm] = useState(null);
  const [code, setCode] = useState('');
  const [timeToConfirmCode, setTimeToConfirmCode] = useState(false);

  // Submit phone number to Firebase Authentication
  async function signInWithPhoneNumber() {
    console.log('signWithPhoneNumber');
    console.log(phoneNumber);
    try {
      const confirmation = await auth().signInWithPhoneNumber(phoneNumber);
      setConfirm(confirmation);
      console.log('TimeToConfirmCode = true');
      setTimeToConfirmCode(true);
    } catch (err) {
      alert(err.message);
    }
  }

  // Check that the code received via SMS is correct
  async function confirmCode() {
    try {
      console.log('confirmCode');
      await confirm.confirm(code);
      setTimeToConfirmCode(false);
      console.log('TimeToConfirmCode = false');
    } catch (error) {
      console.log('Invalid code.');
    }
  }

  /* const handleLogin = () => {
    console.log('PhoneSignIn');
    if (!confirm) {
      signInWithPhoneNumber(phoneNumber);
    } else {
      console.log('Rejected');
      console.log(phoneNumber);
    }
  }; */

  if (!timeToConfirmCode) {
    return (
      <KeyboardAvoidingView style={styles.container} behavior="padding">
        <View style={styles.imageContainer}>
          <Image
            style={styles.image}
            source={require('../assets/birdwing.png')}></Image>
        </View>
        <View style={styles.buttonContainer}>
          <Text style={styles.text}>Login</Text>
        </View>
        <View style={styles.inputContainer}>
          <TextInput
            placeholder="Phone number"
            value={phoneNumber}
            onChangeText={text => setPhoneNumber(text)}
            style={styles.input}
          />
        </View>
        <View style={styles.buttonContainer}>
          <TouchableOpacity
            onPress={signInWithPhoneNumber}
            style={[styles.button, styles.buttonOutline]}>
            <Text style={styles.buttonText}>Login</Text>
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
    );
  } else {
    return (
      <KeyboardAvoidingView style={styles.container} behavior="padding">
        <View style={styles.buttonContainer}>
          <Text style={styles.text}>Enter code</Text>
        </View>
        <View style={styles.inputContainer}>
          <TextInput
            placeholder="Code"
            value={code}
            onChangeText={text => setCode(text)}
            style={styles.input}
          />
        </View>
        <View style={styles.buttonContainer}>
          <TouchableOpacity
            onPress={confirmCode}
            style={[styles.button, styles.buttonOutline]}>
            <Text style={styles.buttonText}>Confirm code</Text>
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
    );
  }
};

export default LoginScreen;
