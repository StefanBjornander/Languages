import {StyleSheet} from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  inputContainer: {
    width: '80%',
  },
  input: {
    backgroundColor: 'white',
    paddingHorizontal: 15,
    paddingVertical: 10,
    marginTop: 5,
  },
  buttonContainer: {
    width: '60%',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 40,
  },
  button: {
    backgroundColor: '#0782F9',
    width: '100%',
    alignItems: 'center',
  },
  buttonOutline: {
    borderColor: '#0782F9',
    borderWidth: 2,
    borderRadius: 5,
  },
  buttonText: {
    color: 'white',
    fontWeight: '700',
    fontSize: 16,
  },
  imageContainer: {
    justifyContent: 'flex-start',
    marginBottom: 10,
  },
  image: {
    width: 100,
    height: 120,
  },
  text: {
    fontSize: 16,
    fontWeight: '700',
  },
});

export default styles;
