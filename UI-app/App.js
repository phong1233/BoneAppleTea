import React, { Component } from 'react';
import RecipeContainer from './components/recipeContainer';
import { Text, View } from 'react-native';

export default class HelloWorldApp extends Component {
  render() {
    return (
      <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
        <RecipeContainer/>
      </View>
    );
  }
}
