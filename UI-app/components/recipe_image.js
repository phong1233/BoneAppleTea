import React, {Component} from 'react';
import {Image} from 'react-native';

class Image extends Component {
    render() {
        let pic = {
            uri: 'https://pinchofyum.com/wp-content/uploads/Fruit-Pizza-Design-Square.jpg'
        };

        return <Image source={pic} style={{width: 300, height: 300}} />;
    }
}

export default class Main extends Component {
    render() {
        return (
            <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
                <Image />
            </View>
        );
    }
}