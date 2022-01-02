import React from "react";

class SentimentPredictor extends React.Component {
    constructor() {
        super()
        this.state = {
            review: "",
            sentiment: "",
            probPositiveSentiment: 0,
            probNegativeSentiment: 0,
            predictionTime: 0

        }
        this.HandleChange = this.HandleChange.bind(this)
        this.HandleSubmit = this.HandleSubmit.bind(this)
        this.HandleClick = this.HandleClick.bind(this)
    }

    getsentiment(review){
        fetch("http://localhost:8000/predict/?review="+review)
            .then(response => response.json())
            .then(response => {
                console.log(response)
                const prediction = response.result
                this.setState({
                    sentiment: prediction["sentiment"],
                    probPositiveSentiment: prediction["positive prediction"],
                    probNegativeSentiment: prediction["negative prediction"],
                    predictionTime: prediction["time"]
                })
        })
    }

    // componentDidMount() {
    //     setTimeout(() => {
    //         this.setState({
    //             isLoading: false
    //         })
    //     }, 1500);
    // }

    HandleChange(event) {
        const {name, value} = event.target
        this.setState({
            [name]: value 
        })
    }

    HandleSubmit(event) {
        event.preventDefault()
        this.getsentiment(this.state.review)
    }
    
    HandleClick(){
        this.setState({
            review: "",
            sentiment: "",
            probPositiveSentiment: 0,
            probNegativeSentiment: 0,
            predictionTime: 0
        })
    }

    render() {
        return(
        <div>
            <form className="mr-form" onSubmit={this.HandleSubmit}>
                <input
                    type="text"
                    name="review"
                    value={this.state.review}
                    placeholder="Enter Your Review"
                    onChange={this.HandleChange}
                />
                <button>PREDICT</button>
                <button onClick={this.HandleClick}>RESET</button>
            </form>
            <p>Review: {this.state.review}</p>
            <div>
                <p>Sentiment: {this.state.sentiment}</p>
                <p>Positive Prediction: {this.state.probPositiveSentiment}</p>
                <p>Negative Prediction: {this.state.probNegativeSentiment}</p>
                <p>Prediction Time: {this.state.predictionTime}</p>
            </div>
        </div>
        )
    }
}

export default SentimentPredictor