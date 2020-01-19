import React, {Component} from 'react';
import RecipeImage from './recipe_image';
import {View, Text, Button, Alert} from 'react-native';

class RecipeContainer extends Component {
    render() {
        return (
            <View style={{paddingTop:40, height: 500, padding:10}}>
                <Text style={{fontFamily:"Courier New", fontSize:13}}>{this.props.recipe.title}</Text>
                <RecipeImage image={this.props.recipe.picture_link} ingredients={this.props.recipe.ingredients}/>
                <View style={{justifyContent:'space-evenly', flexDirection:'row'}}>
                    <Button
                    title="Press me"
                    onPress={console.log('hello')}
                    />
                    <Button
                    title="Press me"
                    onPress={() => Alert.alert('Simple Button pressed')}
                    />
                </View>
            </View>
        );
    }
}

export default RecipeContainer;