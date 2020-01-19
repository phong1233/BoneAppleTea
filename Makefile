init:
	( cd UI-app && npm install && npm install react-native-deck-swiper --save && npm i react-native-realistic-deck-swiper &&  npm install --save react-native-vector-icons && npm install --save react-native-swipe-cards)

start-front:
	( cd UI-app && npx react-native run-ios )