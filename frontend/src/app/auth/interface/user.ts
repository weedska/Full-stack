export interface User {
  number :
  {
    id: number;
  posts_disliked: Array<{}>;
  posts_liked: Array<{}>;
  profile: {
    bio: string;
    birth_date: Date;
    location: string;
    photo: string;
  };
  user_followers: Array<{}>;
  user_posts: Array<{}>;
  username: string
  }



}

export interface Token {
  token: string
}
