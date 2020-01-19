import React from 'react'
import { View, Text } from 'react-native'
import Swiper from 'react-native-realistic-deck-swiper'
import RecipeContainer from './recipeContainer'

let Data = [];
let counter = -1;
  export default class App extends React.Component {
    componentDidMount(){
        Data = this.props.recipes;
    }
    _renderCard = (item) => {
      counter += 1;
      if(Data.length == 0){
          return null;
      }
      console.log(Data.length);
      console.log(counter);

    //   console.log(Data[counter] + '\n\n\n\n\n\n');
      return <RecipeContainer recipe={Data[counter%10]}/>
    }
    render() {
      return (
        <View style={{ flex: 1 }}>
          <Swiper
            infiniteSwipe={true}
            startIndex={0}
            cardsData={this.props.recipes}
            renderCard={this._renderCard}
            containerStyle={{
              flex: 1,
              alignItems: 'center',
              justifyContent: 'center',
            }}
            style={{
              margin: 20,
              backgroundColor: 'white',
              borderColor: 'black',
              borderWidth: 1,
              borderRadius: 5,
            }}
          />
        </View>
      );
    }
  }