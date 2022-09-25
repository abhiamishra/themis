export function mapper (arr) {
    return (
        <div className="justices">
          {arr.map((justice, index) => (
            <div key={index}>
                <p>{justice.name}</p>
                <p>{justice.opinion}</p>
            </div>
          ))}
        </div>)
};