import React from 'react';
import {Text, View, Image, TouchableOpacity} from 'react-native';
import auth from '@react-native-firebase/auth';
import styles from '../settings/Styles';

const HomeScreen = () => {
  const handeLogout = () => {
    auth()
      .signOut()
      .then(() => {
        console.log('Logged out');
      })
      .catch(error => log.console(error.message));
  };

  return (
    <View style={styles.container}>
      <View style={styles.imageContainer}>
        <Image
          style={styles.image}
          source={require('../assets/birdwing.png')}></Image>
      </View>
      <Text style={styles.text}>You are now logged in.</Text>
      <View style={styles.buttonContainer}>
        <TouchableOpacity
          style={[styles.button, styles.buttonOutline]}
          onPress={handeLogout}>
          <Text style={styles.buttonText}>Log out</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default HomeScreen;
