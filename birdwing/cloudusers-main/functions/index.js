const functions = require("firebase-functions");
const admin = require("firebase-admin");
const { initializeApp } = require("firebase-admin/app");
//var serviceAccount = require("../firebase-adminsdk.json");
const { credential } = require("firebase-admin");
const {
  getFirestore,
  serverTimestamp,
  FieldValue,
} = require("firebase-admin/firestore");

/* admin.initializeApp({
  projectId: "birdwing-cc771",
  credential: admin.credential.cert(serviceAccount),
}); */

admin.initializeApp();
const db = admin.firestore();

// Checks if a user exists in users collection for a given uid
exports.existsInUsers = functions
  .region("europe-west1")
  .https.onCall(async (data, context) => {
    functions.logger.log("uid = ", data);
    const { uid } = data;
    await db
      .collection("users")
      .doc(data)
      .get()
      .then((documentSnapshot) => {
        return documentSnapshot.exists;
      });
  });

// Runs when a new user is created in firebase auth.
// Creates a new entry in firestore users collection with the uid from firebase auth
exports.register = functions
  .region("europe-west1")
  .auth.user()
  .onCreate(async (user) => {
    await db.collection("users").doc(user.uid).set({
      created: FieldValue.serverTimestamp(),
    });
  });

// Runs when a user is deleted from firebase auth
// Deletes the associated user in firestore users collection
exports.deleteUser = functions
  .region("europe-west1")
  .auth.user()
  .onDelete(async (user) => {
    await db.collection("users").doc(user.uid).delete();
  });
