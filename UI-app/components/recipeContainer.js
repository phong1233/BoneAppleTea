import React, {Component} from 'react';
import RecipeImage from './recipe_image';
import {View, Text, Image} from 'react-native';

class RecipeContainer extends Component {
    render() {
        return (
            <View style={{backgroundColor:'red'}}>
                <RecipeImage/>
            </View>
        );
    }
}

export default RecipeContainer;