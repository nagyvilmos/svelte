// 

export const doRequest = (uri, onSuccess=undefined, onError=undefined, {payload={}, parameters={}, method="GET", header={}, isJson=true}) => {
  const fullUri = uri + buildQuery(parameters);
    fetch(`./api/${fullUri}`)
    .then((response) => {
      if (isJson)
      {
        response.json().then(data => {
          console.debug({ data });
          onSuccess && onSuccess(data);
        })    .catch((ex) => {
          console.error({ ex });
          onError && onError(ex)
        });    
      }
      else
      {
        onSuccess && onSuccess(response);
      }
    })
    .catch((ex) => {
      console.error({ ex });
      onError && onError(ex)
    });
}

const buildQuery = (parameters) => {
  const queryArgs = Object.keys(parameters).map(key => {
    const value = parameters[key];
    if (!Array.isArray(value)) {
      return `${key}=${encodeURIComponent(value)}`;
    } else {
      return value
        .map((i) => {
          return `${key}=${encodeURIComponent(value[i])}`;
        })
        .join("&");
    }
  }).join("&");
  return queryArgs.length > 0 ? `?${queryArgs}` : "";
}