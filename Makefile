init:
	( cd Frontend && npm install && cd ios && pod install )

start-ui:
	( cd Frontend && npx react-native run-ios )

start-back:
	(cd Backend && python3 app.py )