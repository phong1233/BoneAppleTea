import React, {Component} from 'react';
import {Image, View, Button, Text, TouchableHighlight, ScrollView} from 'react-native';
import FlatList from './flatlist';

class ImageApp extends Component {
    render() {
        let pic = {
            uri: 'https://pinchofyum.com/wp-content/uploads/Fruit-Pizza-Design-Square.jpg'
        };
        return (
            <View>
                <Image source={pic} style={{width: 300, height: 300, borderRadius: 15}} />
            </View>
        );

    }
}

export default class RecipeImage extends Component {
    state = {buttonPressed: false};
    
    onPress = () => {
        this.setState({
            buttonPressed: !this.state.buttonPressed
        });
    }

    render() {
        
        if(!this.state.buttonPressed) {
            return (
                <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
                    <TouchableHighlight onPress={this.onPress} activeOpacity={0}>
                        <ImageApp />
                    </TouchableHighlight>
                </View>
            );
        }

        return (
            <View style={{width: 300, height: 300, flex: 1, justifyContent: "center", alignItems: "center" }}>
                <TouchableHighlight onPress={this.onPress} activeOpacity={0}>
                    <ScrollView style={{width:300, height: 300}}
                        data={[
                            {key: 'Devin'},
                            {key: 'Dan'},
                            {key: 'Dominic'},
                            {key: 'Jackson'},
                            {key: 'James'},
                            {key: 'Joel'},
                            {key: 'John'},
                            {key: 'Jillian'},
                            {key: 'Jimmy'},
                            {key: 'Julie'},
                        ]}
                        renderItem={({item}) => <Text style={{color:'black'}}>{item.key}</Text>}
                    />
                </TouchableHighlight>
            </View>
        );
    }
}
