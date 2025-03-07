import React from 'react';

const AIAnalysis = ({ speedResult }) => {
    const [suggestions, setSuggestions] = React.useState([]);

    const handleAnalysis = async () => {
        const response = await fetch('http://localhost:8000/ai_analysis', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(speedResult)
        });
        const data = await response.json();
        setSuggestions(data.suggestions);
    };

    return (
        <div>
            <button onClick={handleAnalysis}>Get AI Suggestions</button>
            <ul>
                {suggestions.map((suggestion, index) => (
                    <li key={index}>{suggestion}</li>
                ))}
            </ul>
        </div>
    );
};

export default AIAnalysis;