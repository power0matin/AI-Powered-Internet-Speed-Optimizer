import React from 'react';

const Optimizations = () => {
    const handleOptimize = async () => {
        const response = await fetch('http://localhost:8000/optimize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ optimize: true })
        });
        const data = await response.json();
        alert(data.message);
    };

    return (
        <div>
            <button onClick={handleOptimize}>Apply Network Optimizations</button>
        </div>
    );
};

export default Optimizations;