// Gói JS riêng của bản app: Firebase (bảng xếp hạng) + plugin App của Capacitor (nút Back).
import firebase from "firebase/compat/app";
import "firebase/compat/auth";
import "firebase/compat/firestore";
import { App } from "@capacitor/app";
window.firebase = firebase;
window.BF_CapApp = App;
