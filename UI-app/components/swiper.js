import React, { Component } from 'react'
import RecipeContainer from './recipeContainer'
import RecipeImage from './recipe_image'
import Swiper from 'react-native-deck-swiper'
import List from './recipe'
import { Button, StyleSheet, Text, View, Switch } from 'react-native'

export default class Swiping extends Component {
  constructor (props) {
    super(props)
    this.state = {
      cards: [],
      swipedAllCards: false,
      swipeDirection: '',
      cardIndex: 0,
      renderRecipe: false
    }
  }
  
  componentDidCatch = () => {
    this.setState({
        cards: this.props.cards
    }, () => {
        console.log(this.state.cards, 'cards2');
        this.forceUpdate();
    }); 
  };
  

  renderCard = (card, index) => {
    console.log('\n\n\n\n\n\n\n\n\n\n\n\n');
    console.log(card);
    console.log('\n\n\n\n\n\n\n\n\n\n\n\n');

    if (!this.state.renderRecipe){
      return (
        <View style={styles.card}>
    <Text style={{textAlign:'center', fontSize:40, borderColor:'blue', margin:20, borderWidth:2}}>{this.state.cards[0]['name']}</Text>
          <RecipeImage/>
        </View>
      )
    }
    return (
      <View style={styles.card}>
        <List />
      </View>
    )
    
  };

  onSwiped = (type) => {
    console.log(`on swiped ${type}`)
  }

  onSwipedAllCards = () => {
    this.setState({
      swipedAllCards: true
    })
  };

  swipeLeft = () => {
    this.swiper.swipeLeft()
  };

  render () {
    return (
      <View style={styles.container}>
        <Swiper
          ref={swiper => {
            this.swiper = swiper
          }}
          onSwipedLeft={() => this.onSwiped('left')}
          onSwipedRight={() => this.onSwiped('right')}
          disableTopSwipe={true}
          disableBottomSwipe={true}
          onTapCard={this.swipeLeft}
          cards={this.state.cards}
          cardIndex={this.state.cardIndex}
          cardVerticalMargin={80}
          renderCard={this.renderCard}
          onSwipedAll={this.onSwipedAllCards}
          stackSize={3}
          stackSeparation={15}
          overlayLabels={{
            left: {
              title: 'NOPE',
              style: {
                label: {
                  backgroundColor: 'black',
                  borderColor: 'black',
                  color: 'white',
                  borderWidth: 1
                },
                wrapper: {
                  flexDirection: 'column',
                  alignItems: 'flex-end',
                  justifyContent: 'flex-start',
                  marginTop: 30,
                  marginLeft: -30
                }
              }
            },
            right: {
              title: 'LIKE',
              style: {
                label: {
                  backgroundColor: 'black',
                  borderColor: 'black',
                  color: 'white',
                  borderWidth: 1
                },
                wrapper: {
                  flexDirection: 'column',
                  alignItems: 'flex-start',
                  justifyContent: 'flex-start',
                  marginTop: 30,
                  marginLeft: 30
                }
              }
            }
          }}
          animateOverlayLabelsOpacity
          animateCardOpacity
          swipeBackCard
        >
          <Button onPress={() => this.swiper.swipeBack()} title='Swipe Back' />
        </Swiper>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5FCFF'
  },
  card: {
    flex: 1,
    borderRadius: 15,
    borderWidth: 2,
    borderColor: '#E8E8E8',
    justifyContent: 'center',
    backgroundColor: 'white',
    paddingTop: 100
  }
})