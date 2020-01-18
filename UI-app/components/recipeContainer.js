import React, {Component} from 'react';
import RecipeImage from './recipe_image';
import {View, Text, Image} from 'react-native';

class RecipeContainer extends Component {
    state = {
        color: ''
    }

    componentDidMount() {
        let color = ''
        switch(this.props.difficulty) {
            case '1':
              color = 'green'
              break;
            case '2':
                color = 'yellow'
              break;
            default:
                color = 'red'
        }
        this.setState({color:color})
    }
    render() {
        return (
            <View style={{paddingTop: 60, padding:30, margin:150, backgroundColor: this.state.color, borderRadius: 15, justifyContent: "center", alignItems: "center"}}>
                <View style={{width:300, justifyContent: "center", alignItems: "center", flex:1}}>
        <Text style={{fontSize: 40, textAlign: 'center'}}>{this.props.name}</Text>
                </View>
                <RecipeImage style={{flex:2}}/>
            </View>
        );
    }
}

export default RecipeContainer;