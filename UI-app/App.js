import React, {Component} from 'react';
import {Text, View, Image} from 'react-native';

class ImageApp extends Component {
  render() {
      let pic = {
          uri: 'https://pinchofyum.com/wp-content/uploads/Fruit-Pizza-Design-Square.jpg'
      };

      return <Image source={pic} style={{width: 300, height: 300, borderRadius: 15}} />;
  }
}

export default class HelloWorldApp extends Component {
  render() {
    return (
      <View style={{ flex: 1, justifyContent: "center", alignItems: "center", backgroundColor: "lightgrey" }}>
        <ImageApp />
      </View>
    );
  }
}
